from textual.app import ComposeResult
from textual.widgets import Header
from textual.widgets import Footer


class Composable:
    def compose(self) -> ComposeResult:
        yield from self.compose_header()
        yield from self.compose_body()
        yield from self.compose_footer()

    def compose_header(self) -> ComposeResult:
        yield Header()

    def compose_body(self) -> ComposeResult:
        raise NotImplementedError

    def compose_footer(self) -> ComposeResult:
        yield Footer()
