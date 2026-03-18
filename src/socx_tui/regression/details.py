from __future__ import annotations

from textwrap import wrap
from typing import ClassVar

from rich.text import Text
from textual import work
from textual.reactive import reactive
from textual.app import ComposeResult
from textual.binding import BindingType
from textual.widget import Widget
from textual.widgets import Markdown
from socx import Regression, TestBase, TestResult, TestStatus, Script

from socx_tui.regression.bindings.vim.mode import VimModes


class RegressionDetails(Widget, can_focus=True, inherit_bindings=True):
    BINDINGS: ClassVar[list[BindingType]] = Markdown.BINDINGS + VimModes.Normal

    DEFAULT_CSS: ClassVar[str] = """
    RegressionDetails {
        content-align: center middle;
    }
    """

    model: reactive[TestBase | None] = reactive(None)

    def __init__(self, *args, wrap_code: bool = True, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._refresh_timer = None
        self._wrap_code = wrap_code
        self._document = Markdown()

    @property
    def document(self) -> Markdown:
        return self._document

    def compose(self) -> ComposeResult:
        yield self._document

    def watch_model(self, model: TestBase) -> None:
        self.document.update(self.format_details(self.model))

    def refresh_details(self) -> None:
        self.show_details(self.model)

    @work(exclusive=False)
    async def show_text(self, message: str | Text) -> None:
        if isinstance(message, Text):
            message = message.plain
        await self.document.update(message)

    @work(exclusive=False)
    async def show_details(self, model: TestBase | None) -> None:
        self.show_text(self.format_details(model))

    def format_details(self, model: TestBase | None = None) -> str:
        if model is None:
            return "\n\n".join(
                [
                    "No regression selected.",
                    "Load a regression file with o or ctrl+o.",
                ]
            )

        lines = [
            f"# {model.name} ({type(model).__name__})",
        ]

        if isinstance(model, Regression):
            kind = (
                "regressions" if self.contains_regressions(model) else "tests"
            )
            lines.extend(
                [
                    f"**👨‍👩‍👧‍👦 Children:** {len(model.tests)} {kind}",
                    f"**❌ Failed:** {self.count_results(model, TestResult.Failed)}",  # noqa: E501
                    f"**✅ Passed:** {self.count_results(model, TestResult.Passed)}",  # noqa: E501
                    f"**💡 Status:** {self.format_status(model.status)}",
                    f"**🚩 Result:** {self.format_result(model.result)}",
                    # f"**⌛ Elapsed Time:** {self.format_timedelta(model.time_elapsed)}",  # noqa: E501, W505
                    f"**⌛ Started Time:** {self.format_time(model.started_time)}",  # noqa: E501
                    f"**⌛ Finished Time:** {self.format_time(model.finished_time)}",  # noqa: E501
                ]
            )
        else:
            lines.extend(
                [
                    f"**💡 Status:** {self.format_status(model.status)}",
                    f"**🚩 Result:** {self.format_result(model.result)}",
                    # f"**⌛ Elapsed Time:** {self.format_timedelta(model.time_elapsed)}",  # noqa: E501, W505
                    f"**⌛ Started Time:** {self.format_time(model.started_time)}",  # noqa: E501
                    f"**⌛ Finished Time:** {self.format_time(model.finished_time)}",  # noqa: E501
                    "",
                    f"**📜 Script:** {self.format_script(model.exec)}",
                ]
            )
        return "\n\n".join(lines)

    def contains_regressions(self, regression: Regression) -> bool:
        return bool(regression.tests) and any(
            isinstance(test, Regression) for test in regression.tests
        )

    def format_script(self, script: Script | None) -> str:
        script_str = str(script or "")
        if self._wrap_code:
            lines = ["\n".join(wrap(line)) for line in script_str.splitlines()]
            script_str = "\n".join(lines)
        return "\n\n".join(["", "```bash", script_str, "```"])

    def format_result(self, result: TestResult | str) -> str:
        if isinstance(result, TestResult):
            return result.value
        return str(result)

    def format_status(self, status: int | str | TestStatus) -> str:
        if isinstance(status, int):
            status = TestStatus(status)
        if isinstance(status, str):
            status = TestStatus[status.strip().lower().title()]
        return status.name.lower()

    def format_time(self, value: float | None) -> str:
        return "n/a" if value is None else f"{value:.3f}"

    def format_timedelta(self, value: int | float | None) -> str:
        if value is None:
            return "n/a"
        total_seconds = int(value)
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        return f"{hours:02}h:{minutes:02}m:{seconds:02}s"

    def count_results(self, regression: Regression, result: TestResult) -> int:
        return sum(1 for test in regression.tests if test.result is result)
