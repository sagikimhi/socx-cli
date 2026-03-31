from __future__ import annotations

from typing import Any, ClassVar
from datetime import datetime
from textwrap import dedent

from rich.markdown import Markdown
from textual import work
from textual.app import RenderResult, ComposeResult
from textual.widgets import Static, ProgressBar, Label
from textual.reactive import reactive
from textual.containers import ScrollableContainer, Horizontal, Center, Middle

from socx import Test, Script, TestBase, Regression, TestResult, TestStatus
from socx_tui.regression.bindings import VimModes


class LabeldProgress(Horizontal, can_focus=False):
    model: reactive[Any] = reactive(None)
    total: reactive[int] = reactive(0)
    completed: reactive[int] = reactive(0)

    def compose(self) -> ComposeResult:
        yield Label(
            id="regression-progress-label",
            name="regression-progress-label",
        )
        yield ProgressBar(id="regression-progress", name="regression-progress")

    def watch_model(self, model) -> None:
        self.total = len(model) if isinstance(model, Regression) else 0
        self.completed = (
            self.count_results(model) if isinstance(model, Regression) else 0
        )

    async def watch_total(self, total: int) -> None:
        self.query_one(ProgressBar).total = total
        await self.update_label()

    async def watch_completed(self, completed: int) -> None:
        self.query_one(ProgressBar).progress = completed
        await self.update_label()

    async def update_label(self) -> None:
        label = self.query_one(Label)
        label.update(
            f"{self.completed}/{self.total} " if self.total != 0 else "--/-- "
        )

    def count_results(self, model: TestBase) -> int:
        if isinstance(model, Regression):
            return len(model) - sum(
                1 if test.result is TestResult.NA else 0
                for test in model.tests
            )
        return 0


class RegressionDetails(
    ScrollableContainer, can_focus=True, inherit_bindings=True
):
    BINDINGS = ScrollableContainer.BINDINGS + VimModes.Normal
    ALLOW_MAXIMIZE: ClassVar[bool] = True

    model: reactive[Any] = reactive(None)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._details = RegressionStaticDetails(id="regression-static-details")
        self._progress = LabeldProgress(
            name="regression-progress", id="regression-progress"
        )

    @property
    def title(self) -> Static:
        return self.query_exactly_one("#regression-details-title", Static)

    @property
    def details(self) -> RegressionStaticDetails:
        return self.query_exactly_one(RegressionStaticDetails)

    @property
    def progress(self) -> LabeldProgress:
        return self.query_exactly_one(LabeldProgress)

    def compose(self):
        with Center(), Middle():
            yield Static(
                Markdown(RegressionStaticDetails.format_header(None)),
                id="regression-details-title",
                name="regression-details-title",
            )
            yield self._details
            yield self._progress

    async def watch_model(self, model: TestBase) -> None:
        async with self.batch():
            self.details.model = model
            self.progress.model = model
            self.details.refresh()
            await self._refresh_progress(model)
            if self.progress.visible:
                self.progress.scroll_visible()

    async def _refresh_progress(self, model: TestBase) -> None:
        if isinstance(model, Regression):
            self.progress.visible = True
        else:
            self.progress.visible = False


class RegressionStaticDetails(Static):
    model: reactive[Any] = reactive(None)
    status: reactive[str] = reactive[str]("")
    result: reactive[str] = reactive[str]("")
    script: reactive[str] = reactive[str]("")
    child_summary: reactive[str] = reactive[str]("")
    exit_code: reactive[str] = reactive[str]("")
    elapsed_time: reactive[str] = reactive[str]("")
    started_time: reactive[str] = reactive[str]("")
    finished_time: reactive[str] = reactive[str]("")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def render(self) -> RenderResult:
        self.update_details()
        return self.format_details(self.model)

    def watch_model(self, model: TestBase) -> None:
        self.update_details()

    @work(exclusive=True, exit_on_error=False)
    async def update_details(self) -> None:
        model = self.model
        async with self.batch():
            if isinstance(model, Test):
                self.exit_code = self.format_retcode(model.retcode)
                self.script = self.format_script(model.exec)

            if model is not None:
                self.status = model.status.name
                self.result = model.result.name
                self.elapsed_time = self.format_timedelta(model.elapsed_time)
                self.started_time = self.format_time(model.started_time)
                self.finished_time = self.format_time(model.finished_time)
            self.child_summary = (
                self.format_children(model)
                if isinstance(model, Regression)
                else ""
            )

    def format_details(self, model: TestBase | None = None) -> RenderResult:
        if model is None:
            text = """
                Use `o` or `ctrl+o` key to load a regression.

                Supported file formats are: yaml, toml, json, ini, and python

                ### Example:

                ```yaml
                my_regression:
                  - name: foo_test
                    exec: |
                      #!/bin/bash
                      /my/custom/run_script --test foo_test

                  - name: bar_test
                    exec: |
                      #!/bin/bash
                      /my/custom/run_script --test bar_test
                ```

                """

        elif isinstance(model, Regression):
            text = "\n\n".join(
                [
                    f"💡 Status: {self.status}",
                    f"🚩 Result: {self.result}",
                    f"👨‍👩‍👧‍👦 Children: {self.child_summary}",
                    f"⌛ Elapsed Time: {self.elapsed_time}",
                    f"⌛ Started Time: {self.started_time}",
                    f"⌛ Finished Time: {self.finished_time}",
                ]
            )
        elif isinstance(model, Test):
            text = "\n\n".join(
                [
                    f"💡 Status: {self.status}",
                    f"🚩 Result: {self.result}",
                    f"🧑‍💻 Exit Code: {self.exit_code}",
                    f"⌛ Elapsed Time: {self.elapsed_time}",
                    f"⌛ Started Time: {self.started_time}",
                    f"⌛ Finished Time: {self.finished_time}",
                    f"📜 Command/Script: {self.script}",
                ]
            )
        else:
            text = ""
        return Markdown(dedent(text))

    def contains_regressions(self, model: TestBase) -> bool:
        return (
            isinstance(model, Regression)
            and bool(model.tests)
            and any(isinstance(test, Regression) for test in model.tests)
        )

    @classmethod
    def format_header(cls, model: TestBase | None) -> str:
        if model is None:
            icon = ""
            text = "Select Regression"
        else:
            text = f"{model.name} ({type(model).__name__})"

        if isinstance(model, Test):
            icon = "🧪 "
        elif isinstance(model, Regression):
            icon = "⚗️ "
        return f"# {icon}{text}"

    def format_children(self, model: Regression) -> str:
        kind = "regressions" if self.contains_regressions(model) else "tests"
        return f"{len(model)} {kind}"

    def format_script(self, script: Script | None) -> str:
        script_str = str(script or "")
        return f"```sh\n\n{script_str}```"

    def format_retcode(self, retcode: int | None) -> str:
        return str(retcode)

    def format_result(self, result: TestResult | str) -> str:
        if isinstance(result, TestResult):
            return result.name
        return TestResult[result.strip().title()].name

    def format_status(self, status: int | str | TestStatus) -> str:
        if isinstance(status, int):
            status = TestStatus(status)
        if isinstance(status, str):
            status = TestStatus[status.strip().title()]
        return status.name

    def format_time(self, value: float | None) -> str:
        if value is None:
            return "n/a"

        try:
            if value >= 946684800:
                return (
                    datetime.fromtimestamp(value)
                    .astimezone()
                    .strftime("%Y-%m-%d %H:%M:%S %Z")
                )
        except (OverflowError, OSError, ValueError):
            pass

        return f"{value:.3f}s"

    def format_timedelta(self, value: int | float | None) -> str:
        if value is None:
            return "n/a"
        total_seconds = int(value)
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        return f"{hours:02}h:{minutes:02}m:{seconds:02}s"

    def count_results(self, regression: Regression, result: TestResult) -> int:
        return sum(
            1 for test in regression.iter_leaf_tests() if test.result is result
        )

    def format_progress(self, regression: Regression, width: int = 24) -> str:
        total = regression.total_test_count
        completed = regression.completed_test_count
        ratio = regression.progress_ratio
        filled = min(width, round(ratio * width))
        bar = "#" * filled + "-" * (width - filled)
        percent = int(ratio * 100)
        return f"[{bar}] {completed}/{total} ({percent}%)"
