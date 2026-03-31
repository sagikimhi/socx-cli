from __future__ import annotations
from textual.widgets.tree import TreeNode

import logging
from functools import partial
from datetime import datetime
from pathlib import Path
from typing import Any, ClassVar

import rich.repr
from rich.text import Text
from socx import (
    Regression,
    Test,
    TestBase,
    TestResult,
    settings,
    enums,
    TestStatus,
)
from textual import on, work
from textual.message import Message
from textual.app import ComposeResult
from textual.binding import Binding, BindingType
from textual.containers import Container
from textual.widget import Widget
from textual.widgets import Button, Tree, Static
from textual_fspicker import FileOpen
from textual_fspicker.path_filters import Filters, Filter

from socx_tui.regression.tree import VimTree
from socx_tui.regression.dialog import TestOutputDialog, RestartSelectionDialog
from socx_tui.regression.details import RegressionDetails


logger = logging.getLogger(__name__)


class TreeLabel(Static):
    pass


@rich.repr.auto
class RegressionWidget(Widget, can_focus=False, inherit_bindings=True):
    """Render loaded regressions as an expandable tree and details pane."""

    class TestStatusChanged(Message):
        """Posted when a test status has changed."""

        def __init__(
            self,
            model: TestBase,
            old_status: TestStatus,
            status: TestStatus,
        ):
            self.model = model
            self.old_status = old_status
            self.status = status
            super().__init__()

    class TestResultChanged(Message):
        """Posted when a test result has changed."""

        def __init__(
            self,
            model: TestBase,
            old_result: TestResult,
            result: TestResult,
        ):
            self.model = model
            self.old_result = old_result
            self.result = result
            super().__init__()

    BINDINGS: ClassVar[list[BindingType]] = [
        Binding(**binding)
        for binding in settings.regression.tui.keybinds.get(
            "RegressionWidget", []
        )
    ]
    ALLOW_MAXIMIZE: ClassVar[bool] = True

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.node_map: dict[str, TreeNode] = {}
        self.loaded_regression: Regression | None = None
        self.details_view = RegressionDetails(
            id="regression-details",
            name="regression-details",
        )
        self.regression_tree = VimTree(
            "Regressions",
            id="regression-tree",
            name="regression-tree",
        )
        self.content_layout = Container(
            self.regression_tree,
            self.details_view,
            id="regression-content-layout",
            name="regression-content-layout",
        )
        self.buttons = [
            Button(
                "Start\n(s)",
                "success",
                id="start-button",
                name="start-button",
                classes="button",
            ),
            Button(
                "Resume\n(r)",
                "primary",
                id="resume-button",
                name="resume-button",
                classes="button",
            ),
            Button(
                "Pause/Suspend\n(x/p)",
                "warning",
                id="pause-button",
                name="pause-button",
                classes="button",
            ),
            Button(
                " Stop/Kill\n(X/P)",
                "error",
                id="stop-button",
                name="stop-button",
                classes="button",
            ),
            Button(
                "Restart\n(R)",
                "default",
                id="restart-button",
                name="restart-button",
                classes="button",
            ),
        ]
        self.button_layout = Container(
            *self.buttons,
            id="regression-button-layout",
            name="regression-button-layout",
        )

    def compose(self) -> ComposeResult:
        yield self.content_layout
        yield self.button_layout

    @property
    def selected_model(self) -> TestBase | None:
        node: TreeNode | None = self.regression_tree.cursor_node
        data = node.data if node is not None else None
        return data if isinstance(data, TestBase) else None

    @work(exclusive=False, exit_on_error=False)
    async def load_regression_from_file(self) -> None:
        """Open a file selection dialog and load selection as regression."""
        await self.action_stop_selected()
        self.set_loading(True)

        try:
            await self._load_regression_from_file()
        finally:
            self.set_loading(False)
            await self._refresh_tree_state()

    async def on_mount(self) -> None:
        self.regression_tree.focus()
        # self._refresh_timer = self.set_interval(
        #     name="referesh_timer",
        #     interval=1 / 5,
        #     callback=self._refresh_tree_state,
        # )

    @on(Button.Pressed)
    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "start-button":
                self.app.call_next(self.action_start_selected)
            case "stop-button":
                self.app.call_next(self.action_stop_selected)
            case "pause-button":
                self.app.call_next(self.action_pause_selected)
            case "resume-button":
                self.app.call_next(self.action_resume_selected)
            case "restart-button":
                self.app.call_next(self.action_prompt_restart_selected)

    @on(VimTree.OpenCursorNode)
    async def on_open_cursor_node(self, event: VimTree.OpenCursorNode) -> None:
        model = getattr(event.node, "data", None)
        if not isinstance(model, Test):
            return
        event.stop()
        await self.app.push_screen(TestOutputDialog(model))

    @on(TestStatusChanged)
    def on_test_status_changed(self, event: TestStatusChanged) -> None:
        self._update_node_label(event.model)
        self.details_view.details.update_details()

    @on(TestResultChanged)
    async def on_test_result_changed(self, event: TestResultChanged) -> None:
        self._update_node_label(event.model)
        self._update_details_progress(event)
        self.details_view.details.refresh()

    @on(Tree.NodeSelected, "#regression-tree")
    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        model = event.node.data

        if isinstance(model, TestBase):
            self._update_node_label(model)

    @on(Tree.NodeHighlighted, "#regression-tree")
    def on_tree_node_highlighted(self, event: Tree.NodeHighlighted) -> None:
        model = event.node.data
        self.details_view.model = model

        if isinstance(model, TestBase):
            self._update_node_label(model)

    def _on_restart_scope_selected(
        self, model: Regression, scope: str | None
    ) -> None:
        if scope is None:
            return
        self._restart_model(model, scope)

    async def action_load_regression_from_file(self) -> None:
        self.load_regression_from_file()

    async def action_start_selected(self) -> None:
        model = self.selected_model
        if model is None:
            self._no_model_selected_notification()
            return
        self._start_model(model)

    async def action_pause_selected(self) -> None:
        model = self.selected_model
        if model is None:
            self._no_model_selected_notification()
            return
        self._pause_model(model)

    async def action_stop_selected(self) -> None:
        model = self.selected_model
        if model is None:
            self._no_model_selected_notification()
            return
        self._stop_model(model)

    async def action_resume_selected(self) -> None:
        model = self.selected_model
        if model is None:
            self._no_model_selected_notification()
            return
        self._resume_model(model)

    async def action_restart_selected(self) -> None:
        model = self.selected_model
        if model is None:
            self._no_model_selected_notification()
            return
        self._restart_model(model, "all")

    async def action_prompt_restart_selected(self) -> None:
        model = self.selected_model
        if model is None:
            self._no_model_selected_notification()
            return
        if isinstance(model, Test):
            self._restart_model(model, "all")
            return
        elif isinstance(model, Regression):
            await self.app.push_screen(
                RestartSelectionDialog(),
                callback=partial(self._on_restart_scope_selected, model),
            )

    @work(exclusive=False, exit_on_error=False)
    async def _start_model(self, model: TestBase) -> None:
        await model.start()

    @work(exclusive=False, exit_on_error=False)
    async def _pause_model(self, model: TestBase) -> None:
        await model.pause()

    @work(exclusive=False, exit_on_error=False)
    async def _stop_model(self, model: TestBase) -> None:
        await model.stop()

    @work(exclusive=False, exit_on_error=False)
    async def _resume_model(self, model: TestBase) -> None:
        await model.resume()

    @work(exclusive=False, exit_on_error=False)
    async def _restart_model(self, model: TestBase, scope: str) -> None:
        await self._restart_model_by_scope(model, scope)

    async def _restart_model_by_scope(
        self, model: TestBase, scope: str
    ) -> None:
        def selector(t: TestBase, scope: str) -> bool:
            match scope:
                case "all":
                    return True
                case "failed":
                    return t.result is TestResult.Failed
                case "cancelled":
                    return t.status is TestStatus.Terminated
                case _:
                    return False

        if scope == "all":
            await model.restart()
            return

        await model.soft_restart(
            partial(selector, scope=scope), auto_start=False
        )

    @work(
        exclusive=True,
        group="model-messages",
        exit_on_error=False,
    )
    async def _post_status_changed(
        self, model: TestBase, old: TestStatus, current: TestStatus
    ) -> None:
        self.post_message(self.TestStatusChanged(model, old, current))

    @work(
        exclusive=True,
        group="model-messages",
        exit_on_error=False,
    )
    async def _post_result_changed(
        self, model: TestBase, old: TestResult, current: TestResult
    ) -> None:
        self.post_message(self.TestResultChanged(model, old, current))

    def _persist_regression_state(self) -> Path | None:
        if self.loaded_regression is None:
            return None
        file = self.loaded_regression.dump_state()
        msg = f"Saved regression state to '{file}'."
        self.notify(msg)
        logger.debug(msg)
        self.log.info(msg)
        return file

    async def _load_regression_from_file(self) -> None:
        file = await self._open_file_dialog()

        if file is None:
            msg = "Operation cancelled."
            logger.debug(msg)
            self.log.info(msg)
            self.notify(msg, title="Load regression", severity="error")
            return

        msg = f"Loading regression from file: '{file}'..."
        logger.debug(msg)
        self.log.info(msg)
        self.notify(msg, title="Load regression")

        try:
            regression = await self._load_regression_tree_from_file(file)
        except Exception as exc:
            msg = f"Failed to load regression: {exc}"
            logger.exception(msg)
            self.log.error(msg)
            self.notify(msg, title="Load regression", severity="error")
            return

        msg = f"Regression '{regression.name}' loaded successfully."
        logger.debug(msg)
        self.log.info(msg)
        self.notify(msg, title="Load regression")
        self.regression_tree.focus()

    async def _open_file_dialog(self) -> Path | None:
        def predicate(path, extensions):
            return bool(Path(path).suffix in extensions)

        filters = [Filter("All Files", lambda p: True)]

        for member in enums.SettingsFormat:
            filter_ = Filter(
                name=member.name,
                tester=partial(predicate, extensions=member.extensions),
            )
            filters.append(filter_)

        return await self.app.push_screen_wait(
            FileOpen(
                open_button="Open",
                cancel_button="Cancel",
                filters=Filters(*filters),
            )
        )

    async def _load_regression_tree_from_file(self, path: Path) -> Regression:
        """Load regressions or saved state from ``path`` into the tree."""
        regression = Regression.load(path=path)
        if regression.output_dir is None:
            regression.assign_output_dir(
                self._create_session_output_dir(regression)
            )

        self.loaded_regression = regression
        self._populate_tree(regression)
        self._connect_model_signals(regression)
        await self._refresh_tree_state()
        return regression

    def _connect_model_signals(self, model: TestBase) -> None:
        model.status_changed.connect(self._post_status_changed)
        model.result_changed.connect(self._post_result_changed)

        if isinstance(model, Regression):
            for child in model.tests:
                self._connect_model_signals(child)

    def _populate_tree(self, regression: Regression) -> None:
        root = self.regression_tree.root
        root.remove_children()
        root.set_label(regression.name)
        root.expand()
        self.node_map.clear()

        first_node = None
        for item in self._top_level_regressions(regression):
            node = self._add_regression_node(root, item)
            if first_node is None:
                first_node = node

        if first_node is None:
            self._show_details(regression)
        else:
            self.regression_tree.move_cursor(first_node)
            self._show_details(first_node.data)

    def _top_level_regressions(
        self, regression: Regression
    ) -> list[Regression]:
        tests = regression.tests
        if len(tests) == 1 and all(
            isinstance(test, Regression) for test in tests
        ):
            return list(tests)  # ty:ignore[invalid-return-type]
        return [regression]

    def _add_regression_node(
        self,
        parent: TreeNode,
        regression: TestBase,
    ):
        node = parent.add(
            label=self._format_label(regression),
            data=regression,
            allow_expand=(
                isinstance(regression, Regression)
                and bool(len(regression.tests))
            ),
        )
        self.node_map[str(regression.id)] = node

        if not isinstance(regression, Regression):
            return

        for test in regression.tests:
            if isinstance(test, Regression):
                self._add_regression_node(node, test)
                continue

            test_node = node.add(
                label=self._format_label(test),
                data=test,
                allow_expand=False,
            )
            self.node_map[str(test.id)] = test_node

        return node

    async def _refresh_tree_state(self) -> None:
        if not self.is_on_screen:
            return

        regression = self.loaded_regression

        if regression is None:
            return

        async with self.batch():
            model = self.selected_model
            labels_changed = False

            for node in self.node_map.values():
                model = getattr(node, "data", None)
                if isinstance(model, TestBase):
                    label = self._format_label(model)
                    if node.label != label:
                        node.set_label(label)
                        labels_changed = True

            if labels_changed:
                self.refresh()

    def _create_session_output_dir(self, regression: Regression) -> Path:
        now = datetime.now().astimezone()
        output_root = settings.regression.run.output.directory
        base_dir = (
            Path(output_root) if isinstance(output_root, str) else output_root
        )
        return (
            base_dir
            / regression.name
            / now.strftime("%Y-%m-%d")
            / now.strftime("%H-%M-%S")
            / regression.name
        )

    def _show_details(self, model: TestBase | None) -> None:
        self.details_view.model = model

    def _format_label(self, model: TestBase | None) -> Text:
        if isinstance(model, Test):
            return self._format_test_label(model)
        elif isinstance(model, Regression):
            return self._format_regression_label(model)
        else:
            return Text("")

    @work(exclusive=False, group="tree", exit_on_error=False)
    async def _update_node_label(self, model: TestBase) -> None:
        def update_label(node):
            node.set_label(self._format_label(node.data).plain)

        parent = self.node_map[str(model.id)]

        while parent is not None:
            parent.set_label(self._format_label(parent.data))
            parent = parent.parent

    @work(exclusive=False, exit_on_error=False)
    async def _update_details_progress(self, event: TestResultChanged) -> None:
        selected = self.regression_tree.cursor_node

        if selected is not None and isinstance(selected.data, Regression):
            node = self.node_map[str(event.model.id)]

            if selected is not node:
                parent = node

                while parent is not None and parent is not selected:
                    parent = parent.parent

                if parent is not None:
                    self.details_view.progress.completed += (
                        -1 if event.result is TestResult.NA else 1
                    )

    def _format_regression_label(self, regression: Regression) -> Text:
        return Text.assemble(
            f"⚗️ {regression.name} ",
            self._format_regression_status_label(regression),
            style="dim italic"
            if not regression.started
            else "italic green"
            if regression.result is TestResult.Passed
            else "italic red"
            if regression.result is TestResult.Failed
            else "italic yellow",
        )

    def _format_regression_status_label(self, regression: Regression) -> Text:
        kind = (
            "regressions"
            if self._contains_regressions(regression)
            else "tests"
        )
        return Text.assemble(
            f"({len(regression)} {kind}) ",
            self._format_test_status_label(regression),
            style="dim italic white"
            if not regression.started
            else "bold italic green"
            if regression.passed
            else "bold italic red"
            if regression.failed
            else "bold italic yellow",
        )

    def _contains_regressions(self, regression: Regression) -> bool:
        return bool(regression.tests) and any(
            isinstance(test, Regression) for test in regression.tests
        )

    def _format_test_label(self, test: TestBase) -> Text:
        return Text.assemble(
            (f"🧪 {test.name} ", "bold"),
            self._format_test_status_label(test),
            style="dim italic white"
            if not test.started
            else "bold italic green"
            if test.passed
            else "bold italic red"
            if test.failed or test.terminated
            else "bold italic yellow1",
        )

    def _format_test_status_label(self, test: TestBase) -> Text:
        status = f"💡 {self.details_view.details.format_status(test.status)}"
        result = f"🚩 {self.details_view.details.format_result(test.result)}"

        if isinstance(test, Test):
            retcode = f"🧑‍💻 {self.details_view.details.format_retcode(test.retcode)}"  # noqa: E501
            return Text.assemble("[", "|".join([status, result, retcode]), "]")
        else:
            return Text.assemble("[", "|".join([status, result]), "]")

    def _no_model_selected_notification(self) -> None:
        msg = "Select a regression or test first."
        self.notify(msg, severity="warning")
