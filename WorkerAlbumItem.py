import sqlite3
from Worker import Worker
from pathlib import Path
from GlobalType import TaxonomicItem, TaxonomicTree
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtCore import Qt, QSize, QDateTime, QRect

from GlobalType import AlbumInfo


class WorkerAlbumItem(Worker):
    def __init__(self, workPath: Path) -> None:
        self.workPath = workPath
        self.dbPath = self.workPath.joinpath("db/database.db")
        super().__init__()

    def setup(self):
        self.conn = sqlite3.connect(self.dbPath)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        return super().setup()

    def LoadThumb(self, para: tuple[Path, bool]) -> QPixmap:
        path = para[0]
        isMovie = para[1]
        pic = QPixmap(path)
        if not pic.isNull():
            pic = pic.scaled(
                QSize(600, 600), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )
        if isMovie:
            maskPic = QPixmap(self.workPath.joinpath("res/film.png"))
            maskPic = maskPic.scaled(
                QSize(600, 600), Qt.AspectRatioMode.IgnoreAspectRatio
            )
            painter = QPainter(pic)
            painter.drawPixmap(0, 0, maskPic)
        return pic

    def DisplayThumb(self, para: tuple[QPixmap, QSize]) -> QPixmap:
        pic = para[0]
        size = para[1]
        if not pic.isNull():
            pic = pic.scaled(size, Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        return pic

    def GetDiveSite(self, datetime: QDateTime) -> str:
        sql = """
            SELECT GROUP_CONCAT([location] || ', ' || [diveSite]) AS [diveSite]
            FROM [dive_log]
            WHERE [timeIn] < ?
                AND [timeOut] > ?
        """
        datetimeStr = datetime.toString("yyyy-MM-dd HH:mm:ss")
        data = (datetimeStr, datetimeStr)
        self.cur.execute(sql, data)
        row = self.cur.fetchone()

        if row:
            return row["diveSite"]
        else:
            return ""

    def DeleteMedia(self, albumInfo: AlbumInfo):
        try:
            albumInfo.thumbPath.unlink(True)
            albumInfo.albumPath.unlink(True)
            sql = "DELETE FROM [media] WHERE id=?"
            data = (albumInfo.id,)
            self.cur.execute(sql, data)
            self.conn.commit()
            pass
        except:
            pass

    def UpdateTime(self, para: tuple[int, QDateTime]):
        id = para[0]
        datetime = para[1]
        sql = "UPDATE [media] SET [shootTime] = ? WHERE [id]=?"
        data = (datetime.toString("yyyy-MM-dd HH:mm:ss"), id)
        self.cur.execute(sql, data)
        self.conn.commit()

    def ChangeCover(self, para: tuple[int, QPixmap]):
        id = para[0]
        thumb = para[1]
        sql = "SELECT [name] FROM [taxonomic] WHERE [id]=?"
        data = (id,)
        self.cur.execute(sql, data)
        row = self.cur.fetchone()
        try:
            path = self.workPath.joinpath("img/thumb").joinpath(
                f"""{str(row["name"])}.jpg"""
            )
            thumb.save(str(path))
        except Exception as e:
            print(e)
            pass
