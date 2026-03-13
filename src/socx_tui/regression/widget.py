from __future__ import annotations

import logging
from pathlib import Path
from typing import ClassVar

import rich.repr
from rich.text import Text
from socx import Regression, Test, TestBase, TestResult, TestStatus
from textual import work
from textual.app import ComposeResult
from textual.binding import Binding, BindingType
from textual.containers import Container, ScrollableContainer
from textual.widget import Widget
from textual.widgets import Button, Static, Tree
from textual_fspicker import FileOpen

from socx_tui.regression.tree import VimTree


logger = logging.getLogger(__name__)


@rich.repr.auto
class RegressionWidget(Widget, can_focus=True, inherit_bindings=True):
    """Render loaded regressions as an expandable tree and details pane."""

    ALLOW_MAXIMIZE = True

    BINDINGS: ClassVar[list[BindingType]] = [
        Binding(
            key="o",
            show=False,
            action="load_regression_from_file()",
            description="Load regression from file",
        ),
        Binding(
            key="ctrl+o",
            action="load_regression_from_file()",
            description="Load regression from file",
            key_display="o / ctrl+o",
        ),
    ]

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.loaded_regression: Regression | None = None
        self.regression_tree = VimTree("Regressions", id="regression-tree")
        self.regression_tree.show_root = False
        self.details = Static(id="regression-details")
        self.details_view = ScrollableContainer(
            self.details,
            id="regression-details-view",
        )
        self.content = Container(
            self.regression_tree,
            self.details_view,
            id="regression-content",
        )
        self.button_layout = Container(
            Button(
                "Start",
                "default",
                id="start-button",
                name="start-button",
                classes="button",
            ),
            Button(
                "Stop",
                "error",
                id="stop-button",
                name="stop-button",
                classes="button",
            ),
            Button(
                "Restart",
                "primary",
                id="restart-button",
                name="restart-button",
                classes="button",
            ),
            id="button-layout",
            name="button-layout",
            classes="layout",
        )

    def compose(self) -> ComposeResult:
        yield self.content
        yield self.button_layout

    async def on_mount(self) -> None:
        self._show_message("Load a regression file with o or ctrl+o.")
        self.regression_tree.focus()

    async def action_load_regression_from_file(self) -> None:
        self.load_regression_from_file()

    @work(exclusive=True)
    async def load_regression_from_file(self) -> None:
        """Open a file selection dialog and load selection as regression."""
        self.set_loading(True)

        try:
            await self._load_regression_from_file()
        finally:
            self.set_loading(False)

    async def load_regression_from_path(self, path: Path) -> Regression:
        """Load regressions from ``path`` into the tree."""
        regression = Regression.from_file(path=path)
        self.loaded_regression = regression
        self._populate_tree(regression)
        self.regression_tree.focus()
        return regression

    async def _load_regression_from_file(self) -> None:
        file = await self._open_file_dialog()

        if file is None:
            msg = "Operation cancelled."
            self.notify(msg, severity="information", title="Load regression")
            self.log.info(msg)
            return

        self.log.info(f"Loading regression from file '{file}'...")
        try:
            regression = await self.load_regression_from_path(file)
        except Exception as exc:
            msg = f"Failed to load regression: {exc}"
            self.notify(msg, title="Load regression", severity="error")
            logger.exception(msg)
            return

        msg = f"Regression '{regression.name}' loaded successfully."
        self.notify(msg, title="Load regression", severity="information")
        self.log.info(msg)
        self.regression_tree.focus()

    async def _open_file_dialog(self) -> Path | None:
        return await self.app.push_screen_wait(
            FileOpen(open_button="Open", cancel_button="Cancel")
        )

    def on_tree_node_highlighted(
        self, event: Tree.NodeHighlighted[object]
    ) -> None:
        model = event.node.data
        if isinstance(model, TestBase):
            self._show_details(model)

    def on_tree_node_selected(self, event: Tree.NodeSelected[object]) -> None:
        model = event.node.data
        if not isinstance(model, TestBase):
            return

        if isinstance(model, Regression) and event.node.allow_expand:
            event.node.toggle()

        self._show_details(model)

    def _populate_tree(self, regression: Regression) -> None:
        root = self.regression_tree.root
        root.remove_children()
        root.set_label(regression.name)
        root.expand()

        first_node = None
        for item in self._top_level_regressions(regression):
            node = self._add_regression_node(root, item)
            first_node = first_node or node

        if first_node is None:
            self._show_details(regression)
            return

        self.regression_tree.move_cursor(first_node)
        self._show_details(first_node.data)

    def _top_level_regressions(
        self, regression: Regression
    ) -> list[Regression]:
        tests = regression.tests
        if tests and all(isinstance(test, Regression) for test in tests):
            return list(tests)
        return [regression]

    def _add_regression_node(
        self,
        parent,
        regression: Regression,
    ):
        node = parent.add(
            self._format_regression_label(regression),
            data=regression,
            allow_expand=bool(regression.tests),
        )
        for test in regression.tests:
            if isinstance(test, Regression):
                self._add_regression_node(node, test)
                continue
            node.add(
                self._format_test_label(test),
                data=test,
                allow_expand=False,
            )
        return node

    def _format_regression_label(self, regression: Regression) -> Text:
        kind = (
            "regressions"
            if self._contains_regressions(regression)
            else "tests"
        )
        label = Text(regression.name, style="bold")
        label.append(f" ({len(regression.tests)} {kind})", style="dim")
        return label

    def _format_test_label(self, test: Test) -> Text:
        label = Text(test.name)
        status = self._format_status(test.status)
        result = self._format_result(test.result)
        label.append(f" [{status} / {result}]", style="dim")
        return label

    def _show_details(self, model: TestBase | None) -> None:
        if model is None:
            self._show_message("No regression selected.")
            return

        lines = [f"Name: {model.name}", f"Type: {type(model).__name__}"]

        if isinstance(model, Regression):
            kind = (
                "child regressions"
                if self._contains_regressions(model)
                else "tests"
            )
            lines.extend(
                [
                    f"Children: {len(model.tests)} {kind}",
                    f"Status: {self._format_status(model.status)}",
                    f"Result: {self._format_result(model.result)}",
                    f"Started: {self._format_time(model.started_time)}",
                    f"Finished: {self._format_time(model.finished_time)}",
                ]
            )
        else:
            lines.extend(
                [
                    f"Status: {self._format_status(model.status)}",
                    f"Result: {self._format_result(model.result)}",
                    f"Started: {self._format_time(model.started_time)}",
                    f"Finished: {self._format_time(model.finished_time)}",
                    "",
                    "Command:",
                    str(model.exec or ""),
                ]
            )

        self.details.update("\n".join(lines))

    def _show_message(self, message: str) -> None:
        self.details.update(message)

    def _contains_regressions(self, regression: Regression) -> bool:
        return bool(regression.tests) and all(
            isinstance(test, Regression) for test in regression.tests
        )

    def _format_result(self, result: TestResult | str) -> str:
        if isinstance(result, TestResult):
            return result.value
        return str(result)

    def _format_status(self, status: TestStatus | int) -> str:
        if isinstance(status, TestStatus):
            return status.name.lower()
        try:
            return TestStatus(status).name.lower()
        except ValueError:
            return str(status)

    def _format_time(self, value: float | None) -> str:
        return "n/a" if value is None else f"{value:.3f}"
