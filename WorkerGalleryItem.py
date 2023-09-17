import sqlite3
from Worker import Worker
from pathlib import Path
from GlobalType import TaxonomicItem, TaxonomicTree
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QSize


class WorkerGalleryItem(Worker):
    def __init__(self, workPath: Path) -> None:
        self.workPath = workPath
        self.dbPath = self.workPath.joinpath("db/database.db")
        super().__init__()

    def setup(self):
        self.conn = sqlite3.connect(self.dbPath)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        return super().setup()

    def LoadThumb(self, path: Path) -> QPixmap:
        pic = QPixmap(path)
        if not pic.isNull():
            pic = pic.scaled(
                QSize(600, 600), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )
        return pic

    def DisplayThumb(self, para: tuple[QPixmap, QSize]):
        pic = para[0]
        size = para[1]
        if not pic.isNull():
            pic = pic.scaled(size, Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        return pic
