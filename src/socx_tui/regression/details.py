from __future__ import annotations

from typing import Any, ClassVar
from datetime import datetime

from socx import (
    Test,
    TestBase,
    Regression,
    TestResult,
    TestStatus,
    settings,
)
from textual.app import ComposeResult
from textual.widgets import ProgressBar, Static, Markdown
from textual.binding import BindingType
from textual.reactive import reactive
from textual.containers import Horizontal, VerticalScroll

from socx_tui.regression.bindings import VimModes


class RegressionDetails(VerticalScroll, can_focus=True, inherit_bindings=True):
    BINDINGS: ClassVar[list[BindingType]] = (
        VimModes.Normal
        + settings.regression.tui.keybinds.get("RegressionDetails", [])
    )
    ALLOW_MAXIMIZE: ClassVar[bool] = True

    model: reactive[Any] = reactive(None, layout=True)
    details: reactive[str] = reactive[str]("")
    status: reactive[str] = reactive[str]("")
    result: reactive[str] = reactive[str]("")
    script: reactive[str] = reactive[str]("")
    exit_code: reactive[str] = reactive[str]("")
    elapsed_time: reactive[str] = reactive[str]("")
    started_time: reactive[str] = reactive[str]("")
    finished_time: reactive[str] = reactive[str]("")
    passed_count: reactive[str] = reactive[str]("")
    failed_count: reactive[str] = reactive[str]("")
    children_count: reactive[str] = reactive[str]("")

    def __init__(
        self, model: TestBase | None, *args: Any, **kwargs: Any
    ) -> None:
        super().__init__(*args, **kwargs)
        self.model = model
        self.markdown = Markdown(
            id="details-markdown",
            name="details-markdown",
            markdown=self.details,
        )
        self.progress = RegressionProgress(
            id="details-progress",
            name="details-progress",
        )
        self.markdown.show_vertical_scrollbar = True

    def compose(self) -> ComposeResult:
        yield self.markdown
        yield self.progress

    def on_mount(self) -> None:
        self.watch(self, "model", self._update_markdown)
        self.watch(self, "details", self._update_progress)

    async def watch_model(self, model: TestBase | None) -> None:
        self._update_markdown(model)
        self._update_progress(model)

    async def watch_details(self, _: str) -> None:
        self._update_progress(self.model)

    def compute_details(self) -> str:
        return self.format_details()

    def compute_status(self) -> str:
        return self.model.status.name if self.model is not None else ""

    def compute_result(self) -> str:
        return self.model.result.name if self.model is not None else ""

    def compute_script(self) -> str:
        script = (
            str(self.model.exec) or "" if isinstance(self.model, Test) else ""
        )
        return "\n\n".join(["", "```sh", script, "```"])

    def compute_exit_code(self) -> str:
        return str(self.model.retcode) if isinstance(self.model, Test) else ""

    def compute_elapsed_time(self) -> str:
        return (
            self.format_timedelta(self.model.elapsed_time)
            if self.model is not None
            else ""
        )

    def compute_started_time(self) -> str:
        return (
            self.format_time(self.model.started_time)
            if self.model is not None
            else ""
        )

    def compute_finished_time(self) -> str:
        return (
            self.format_time(self.model.finished_time)
            if self.model is not None
            else ""
        )

    def compute_passed_count(self) -> str:
        return (
            self.format_passed_count(self.model)
            if isinstance(self.model, Regression)
            else ""
        )

    def compute_failed_count(self) -> str:
        return (
            self.format_failed_count(self.model)
            if isinstance(self.model, Regression)
            else ""
        )

    def compute_children_count(self) -> str:
        return (
            self.format_children_count(self.model)
            if isinstance(self.model, Regression)
            else ""
        )

    def format_details(self) -> str:
        if self.model is None:
            return self._format_help_details()

        if isinstance(self.model, Test):
            return self._format_test_details()

        return self._format_regression_details()

    def _update_markdown(self, _: TestBase | None) -> None:
        self.query_one(Markdown).update(self.details)

    def _update_progress(self, model: TestBase | None) -> None:
        progress = self.query_one(RegressionProgress)
        if model is not progress.model:
            progress.model = model
        else:
            progress.mutate_reactive(RegressionProgress.model)

    @classmethod
    def _format_help_details(cls) -> str:
        return settings.regression.tui.details.help

    def _format_test_details(self) -> str:
        return "\n\n".join(
            [
                f"# {self.format_header(self.model)}",
                f"💡 Status: {self.status}",
                f"🚩 Result: {self.result}",
                f"🧑‍💻 Exit Code: {self.exit_code}",
                f"⌛ Elapsed Time: {self.elapsed_time}",
                f"⌛ Started Time: {self.started_time}",
                f"⌛ Finished Time: {self.finished_time}",
                f"📜 Command/Script: {self.script}",
            ]
        )

    def _format_regression_details(self) -> str:
        return "\n\n".join(
            [
                f"# {self.format_header(self.model)}",
                f"💡 Status: {self.status}",
                f"🚩 Result: {self.result}",
                f"⌛ Elapsed Time: {self.elapsed_time}",
                f"⌛ Started Time: {self.started_time}",
                f"⌛ Finished Time: {self.finished_time}",
                f"✅ Passed Count: {self.passed_count}",
                f"❌ Failed Count: {self.failed_count}",
                f"👨‍👩‍👧‍👦 Children Count: {self.children_count}",
            ]
        )

    @classmethod
    def format_header(cls, model: TestBase) -> str:
        if isinstance(model, Test):
            return f"🧪 {model.name} ({model._typename()})"

        if isinstance(model, Regression):
            return f"⚗️ {model.name} ({model._typename()})"

        return f"{model.name} ({type(model).__name__})"

    @classmethod
    def format_status(cls, status: int | str | TestStatus) -> str:
        if isinstance(status, str):
            status = TestStatus[status.strip().lower().title()]

        if isinstance(status, int):
            status = TestStatus(status)

        return status.name

    @classmethod
    def format_result(cls, result: int | TestResult) -> str:
        if isinstance(result, int):
            result = TestResult(result)

        return result.name

    @classmethod
    def format_exit_code(cls, code: int | None):
        return str(code) if code is not None else ""

    @classmethod
    def format_time(cls, value: float | None) -> str:
        if value is None:
            return ""

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

    @classmethod
    def format_timedelta(cls, value: int | float | None) -> str:
        if value is None:
            return "n/a"
        total_seconds = int(value)
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        return f"{hours:02}h:{minutes:02}m:{seconds:02}s"

    @classmethod
    def format_passed_count(cls, model: Regression) -> str:
        passed_count = sum(1 if test.passed else 0 for test in model.tests)
        return str(passed_count)

    @classmethod
    def format_failed_count(cls, model: Regression) -> str:
        failed_count = sum(1 if test.failed else 0 for test in model.tests)
        return str(failed_count)

    @classmethod
    def format_children_count(cls, model: Regression) -> str:
        kind = "regressions" if cls.contains_regressions(model) else "tests"
        return f"{len(model)} {kind}"

    @classmethod
    def contains_regressions(cls, model: TestBase) -> bool:
        return (
            isinstance(model, Regression)
            and bool(model.tests)
            and any(isinstance(test, Regression) for test in model.tests)
        )


class RegressionProgress(Horizontal, can_focus=False):
    ALLOW_MAXIMIZE: ClassVar[bool] = False

    model: reactive[Any] = reactive(None, layout=True)
    total: reactive[int] = reactive[int](0)
    completed: reactive[int] = reactive[int](0)

    def compose(self) -> ComposeResult:
        yield Static(
            id="progress-label",
            name="progress-label",
        )
        yield ProgressBar(id="progress-bar", name="progress-bar")

    def watch_model(self, model) -> None:
        self.update_label()
        self.update_progress()

        if isinstance(model, Regression):
            self.visible = True
        else:
            self.visible = False

    def compute_total(self) -> int:
        return len(self.model) if isinstance(self.model, Regression) else 0

    def compute_completed(self) -> int:
        return (
            self.count_results(self.model)
            if isinstance(self.model, Regression)
            else 0
        )

    def update_progress(self) -> None:
        progress = self.query_one_optional(ProgressBar)
        if progress is not None:
            progress.total = self.total
            progress.progress = self.completed
            progress.update()

    def update_label(self) -> None:
        label = self.query_one_optional(Static)
        if label is not None:
            label.update(
                f"{self.completed}/{self.total} "
                if self.total > 0
                else "--/-- "
            )

    def count_results(self, model: TestBase) -> int:
        if isinstance(model, Regression):
            return len(model) - sum(
                1 if test.result is TestResult.NA else 0
                for test in model.tests
            )
        return 0
