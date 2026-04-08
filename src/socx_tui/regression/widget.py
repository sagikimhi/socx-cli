from __future__ import annotations

from functools import partial
from datetime import datetime
from pathlib import Path
from typing import Any, ClassVar

import rich.repr
from rich.text import Text
from textual import on, work
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Button
from textual.widgets.tree import TreeNode
from textual.binding import Binding, BindingType
from textual.message import Message
from textual_fspicker import FileOpen
from textual.containers import Container
from textual_fspicker.path_filters import Filters, Filter
from socx import (
    FilePath,
    Test,
    TestBase,
    TestResult,
    TestStatus,
    Regression,
    enums,
    settings,
    get_logger,
)

from socx_tui.regression.tree import RegressionTree
from socx_tui.regression.dialog import TestOutputDialog, RestartSelectionDialog
from socx_tui.regression.details import RegressionDetails


logger = get_logger(__name__)


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

    def __init__(self, *args, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._refresh_timer = None
        self.loaded_regression = None
        self.node_map: dict[str, TreeNode] = {}
        self.details_view = RegressionDetails(
            None,
            id="regression-details",
            name="regression-details",
        )
        self.regression_tree = RegressionTree(
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
                label="Start\n(s)",
                variant="success",
                id="start-button",
                name="start-button",
                classes="button",
                compact=True,
                flat=True,
            ),
            Button(
                label="Resume\n(r)",
                variant="primary",
                id="resume-button",
                name="resume-button",
                classes="button",
                compact=True,
                flat=True,
            ),
            Button(
                label="Pause/Suspend\n(x/p)",
                variant="warning",
                id="pause-button",
                name="pause-button",
                classes="button",
                compact=True,
                flat=True,
            ),
            Button(
                label="Stop/Terminate\n(X/P)",
                variant="error",
                id="stop-button",
                name="stop-button",
                classes="button",
                compact=True,
                flat=True,
            ),
            Button(
                label="Restart\n(R)",
                variant="default",
                id="restart-button",
                name="restart-button",
                classes="button",
                compact=True,
                flat=True,
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
        return self.get_selected_model()

    def get_selected_model(self) -> TestBase | None:
        node: TreeNode | None = self.regression_tree.cursor_node
        data = node.data if node is not None else None
        return data if isinstance(data, TestBase) else None

    def on_mount(self) -> None:
        self.details_view.focus()
        self._refresh_timer = self.set_interval(1, self._refresh_details)

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

    @on(RegressionTree.OpenCursorNode)
    async def on_open_cursor_node(
        self, event: RegressionTree.OpenCursorNode
    ) -> None:
        model = getattr(event.node, "data", None)
        if model is not None:
            self._open_output_dialog(model)
            event.stop()

    @work(
        name="output",
        group="dialogs",
        exclusive=False,
        exit_on_error=False,
    )
    async def _open_output_dialog(self, model: TestBase) -> None:
        if self._refresh_timer is not None:
            self._refresh_timer.pause()

        await self.app.push_screen(
            TestOutputDialog(model, id="output-dialog", name="output-dialog"),
            wait_for_dismiss=True,
        )

        if self._refresh_timer is not None:
            self._refresh_timer.resume()

    @on(TestStatusChanged)
    async def on_test_status_changed(self, event: TestStatusChanged) -> None:
        self._refresh_tree_node_label(event.model)

    @on(TestResultChanged)
    async def on_test_result_changed(self, event: TestResultChanged) -> None:
        self._refresh_tree_node_label(event.model)

    def _on_restart_scope_selected(
        self, model: Regression, scope: str | None
    ) -> None:
        if scope is None:
            return
        self._restart_model(model, scope)

    async def action_load_regression_from_file(self) -> None:
        self.load_regression_from_file()

    @work(
        name="load_regression",
        group="regression",
        exclusive=True,
        description="Load a new regression from a file.",
        exit_on_error=False,
    )
    async def load_regression_from_file(self) -> None:
        """Open a file selection dialog and load selection as regression."""
        await self.stop_selected()
        self.set_loading(True)

        try:
            await self._load_regression_from_file()
        finally:
            self.set_loading(False)

    async def action_start_selected(self) -> None:
        await self.start_selected()

    async def start_selected(self) -> None:
        async with self.lock:
            model = self.selected_model
        if model is None:
            self._no_model_selected_notification()
            return
        self._start_model(model)

    async def action_pause_selected(self) -> None:
        await self.pause_selected()

    async def pause_selected(self) -> None:
        async with self.lock:
            model = self.selected_model
        if model is None:
            self._no_model_selected_notification()
            return
        self._pause_model(model)

    async def action_resume_selected(self) -> None:
        await self.resume_selected()

    async def resume_selected(self) -> None:
        async with self.lock:
            model = self.selected_model
        if model is None:
            self._no_model_selected_notification()
            return
        self._resume_model(model)

    async def action_stop_selected(self) -> None:
        await self.stop_selected()

    async def stop_selected(self) -> None:
        async with self.lock:
            model = self.selected_model
        if model is None:
            self._no_model_selected_notification()
            return
        self._stop_model(model)

    async def action_restart_selected(self) -> None:
        await self.restart_selected()

    async def restart_selected(self) -> None:
        async with self.lock:
            model = self.selected_model
        if model is None:
            self._no_model_selected_notification()
            return
        self._restart_model(model, "all")

    async def action_prompt_restart_selected(self) -> None:
        await self.prompt_restart_selected()

    async def prompt_restart_selected(self) -> None:
        async with self.lock:
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

    @work(
        exclusive=False, name="start", group="regression", exit_on_error=False
    )
    async def _start_model(self, model: TestBase) -> None:
        await model.start()

    @work(
        exclusive=False, name="pause", group="regression", exit_on_error=False
    )
    async def _pause_model(self, model: TestBase) -> None:
        await model.pause()

    @work(
        exclusive=False, name="stop", group="regression", exit_on_error=False
    )
    async def _stop_model(self, model: TestBase) -> None:
        await model.stop()

    @work(
        exclusive=False, name="resume", group="regression", exit_on_error=False
    )
    async def _resume_model(self, model: TestBase) -> None:
        await model.resume()

    @work(
        exclusive=False,
        name="restart",
        group="regression",
        exit_on_error=False,
    )
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
        name="post_status_changed",
        group="messages",
        exclusive=False,
        exit_on_error=False,
    )
    async def _post_status_changed(
        self, model: TestBase, old: TestStatus, current: TestStatus
    ) -> None:
        self.post_message(self.TestStatusChanged(model, old, current))

    @work(
        name="post_result_changed",
        group="messages",
        exclusive=False,
        exit_on_error=False,
    )
    async def _post_result_changed(
        self, model: TestBase, old: TestResult, current: TestResult
    ) -> None:
        self.post_message(self.TestResultChanged(model, old, current))

    def _persist_regression_state(self) -> Path | None:
        loaded_regression = self.loaded_regression

        if loaded_regression is None:
            return None

        file = loaded_regression.dump_state()
        msg = f"Saved regression state to '{file}'."
        logger.info(msg)
        self.notify(msg)
        self.log.info(msg)
        return file

    async def _load_regression_from_file(self) -> None:
        file = await self._open_file_dialog()

        if file is None:
            msg = "Operation cancelled."
            logger.debug(msg)
            self.log.info(msg)
            self.notify(msg, title="Load regression")
            return

        msg = f"Loading regression from file: '{file}'..."
        logger.info(msg)
        self.log.info(msg)
        self.notify(msg, title="Load regression")

        try:
            regression = await self._load_regression_tree_from_file(file)
        except Exception as exc:
            msg = f"Failed to load regression: {exc}"
            logger.exception(msg)
            self.log.error(msg)
            self.notify(
                msg, title="Load regression", severity="error", markup=False
            )
            return

        msg = f"Regression '{regression.name}' loaded successfully."
        logger.info(msg)
        self.log.info(msg)
        self.notify(msg, title="Load regression")
        self.regression_tree.focus()

    async def _open_file_dialog(self) -> Path | None:
        def predicate(path, extensions):
            return bool(Path(path).suffix in extensions)

        filters = [
            Filter(
                "All Supported Formats",
                partial(
                    predicate, extensions=enums.SettingsFormat.all_extensions()
                ),
            )
        ]

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

    async def _load_regression_tree_from_file(
        self, path: FilePath
    ) -> Regression:
        """Load regressions or saved state from ``path`` into the tree."""
        regression = Regression.load(
            path=path, test_cls=settings.regression.test_cls
        )

        if regression.output_dir is None:
            regression.assign_output_dir(
                self._create_session_output_dir(regression)
            )

        del self.loaded_regression
        self.loaded_regression = regression
        self._populate_tree(regression)
        self._connect_model_signals(regression)
        return regression

    def _connect_model_signals(self, model: TestBase) -> None:
        if isinstance(model, Regression):
            for child in model.tests:
                self._connect_model_signals(child)
        model.status_changed.connect(self._post_status_changed)
        model.result_changed.connect(self._post_result_changed)

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

        if first_node is not None:
            self.regression_tree.move_cursor(first_node)
            self._refresh_details()

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

    @work(
        name="refresh_details",
        group="details",
        exclusive=True,
        exit_on_error=True,
    )
    async def _refresh_details(self, *args, **kwargs) -> None:
        async with self.lock:
            model = self.selected_model

        if model is not self.details_view.model:
            self.details_view.model = model
            return

        if model is not None:
            self.details_view.mutate_reactive(RegressionDetails.model)

    @work(
        exclusive=False, name="refresh_tree", group="tree", exit_on_error=True
    )
    async def _refresh_tree_node_label(self, model: TestBase) -> None:
        key = str(model.id)
        node = self.node_map.get(key)
        node_updated = False

        while node is not None:
            data = node.data
            label = self._format_label(data)

            if node.label == label:
                break

            node.set_label(label)
            node = node.parent
            node_updated = True

        if node_updated:
            self.regression_tree.refresh()

    def _no_model_selected_notification(self) -> None:
        msg = "Select a regression or test first."
        self.notify(msg, severity="warning")

    @classmethod
    def _create_session_output_dir(cls, regression: Regression) -> Path:
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

    @classmethod
    def _format_label(cls, model: TestBase | None) -> Text:
        if isinstance(model, Test):
            return cls._format_test_label(model)
        elif isinstance(model, Regression):
            return cls._format_regression_label(model)
        else:
            return Text("")

    @classmethod
    def _format_regression_label(cls, regression: Regression) -> Text:
        return Text.assemble(
            f"⚗️ {regression.name} ",
            cls._format_regression_status_label(regression),
            style=(
                "italic"
                if not regression.started
                else "italic green"
                if regression.passed
                else "italic red"
                if regression.failed
                else "italic yellow"
            ),
        )

    @classmethod
    def _format_regression_status_label(cls, regression: Regression) -> Text:
        kind = (
            "regressions" if cls._contains_regressions(regression) else "tests"
        )
        return Text.assemble(
            f"({len(regression)} {kind}) ",
            cls._format_test_status_label(regression),
            style="italic"
            if not regression.started
            else "italic green"
            if regression.passed
            else "italic red"
            if regression.failed
            else "italic yellow",
        )

    @classmethod
    def _format_test_label(cls, test: TestBase) -> Text:
        style = (
            "italic"
            if not test.started
            else "italic green"
            if test.passed
            else "italic red"
            if test.failed
            else "italic yellow"
        )
        return Text.assemble(
            (f"🧪 {test.name} ", style),
            (cls._format_test_status_label(test).plain, style),
        )

    @classmethod
    def _format_test_status_label(cls, test: TestBase) -> Text:
        style = (
            "italic"
            if not test.started
            else "italic green"
            if test.passed
            else "italic red"
            if test.failed
            else "italic yellow"
        )
        status = f"💡 {RegressionDetails.format_status(test.status)}"
        result = f"🚩 {RegressionDetails.format_result(test.result)}"

        if isinstance(test, Test):
            retcode = (
                f"🧑‍💻 {RegressionDetails.format_exit_code(test.retcode)}"
            )
            return Text.assemble(
                "[", "|".join([status, result, retcode]), "]", style=style
            )
        else:
            return Text.assemble(
                "[", "|".join([status, result]), "]", style=style
            )

    @classmethod
    def _contains_regressions(cls, regression: Regression) -> bool:
        return bool(regression.tests) and any(
            isinstance(test, Regression) for test in regression.tests
        )
