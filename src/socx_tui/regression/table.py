from pathlib import Path

from socx import Visitor as Visitor
from socx import Regression as Regression
from socx import settings as settings
from textual.widgets import DataTable


class Table(DataTable):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._data_model = None

    @property
    def model(self) -> Regression:
        return self._data_model

    @model.setter
    def model(self, model: Regression) -> None:
        self._data_model = model

    @property
    def settings(self):
        """The settings property."""
        return settings.regression

    def accept(self, visitor: Visitor) -> None:
        if self.model:
            self.model.accept(visitor)

    def load_from_file(self, file: str | Path) -> None:
        if isinstance(file, str):
            file = Path(file).resolve()
        model = Regression.from_lines(
            "table_model", file.read_text().splitlines()
        )
        self.model = model
