import sqlite3
from Worker import Worker
from pathlib import Path
from GlobalType import TaxonomicItem, AlbumData, AlbumInfo
import time
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, QSize, QDateTime
from datetime import datetime
import shutil
import piexif
from moviepy.editor import VideoFileClip
from PIL import Image
import numpy


class WorkerAlbum(Worker):
    def __init__(self, workPath: Path) -> None:
        self.workPath = workPath
        self.dbPath = self.workPath.joinpath("db/database.db")
        super().__init__()

    def setup(self):
        self.conn = sqlite3.connect(self.dbPath)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        return super().setup()

    def GetAlbumData(self, id: int) -> AlbumData:
        sql = """
            SELECT [id]
                ,[name]
                ,[parentId]
                ,[rank]
                ,[commonName]
                ,[otherNames]
                ,[information]
            FROM [taxonomic]
            WHERE [id] = ?        
        """
        data = (id,)
        self.cur.execute(sql, data)
        row = self.cur.fetchone()
        if row:
            taxonomicItem = TaxonomicItem(
                row["id"],
                row["parentId"],
                row["name"],
                row["rank"],
                row["commonName"],
                row["otherNames"],
                row["information"],
            )
        else:
            taxonomicItem = TaxonomicItem()
        thumbPath = self.workPath.joinpath("img/thumb").joinpath(
            f"{taxonomicItem.name}.jpg"
        )
        thumbDir = self.workPath.joinpath("img/thumb").joinpath(f"{taxonomicItem.name}")
        albumDir = self.workPath.joinpath("img/album").joinpath(f"{taxonomicItem.name}")
        thumbPic = QPixmap(thumbPath)
        if not thumbPic.isNull():
            thumbPic = thumbPic.scaled(
                QSize(150, 150), Qt.AspectRatioMode.KeepAspectRatioByExpanding
            )

        sql = """
            SELECT [id]
                ,[taxonomicId]
                ,[albumName]
                ,[thumbName]
                ,strftime('%Y-%m-%d %H:%M:%S', shootTime) AS [shootTime]
                ,[isMovie]
            FROM [media]
            WHERE taxonomicId = ?
            ORDER by [isMovie] ASC
                , [shootTime] DESC
        """
        data = (id,)
        self.cur.execute(sql, data)
        rows = self.cur.fetchall()
        albumInfoList: list[AlbumInfo] = []
        for row in rows:
            albumInfo = AlbumInfo(
                row["id"],
                row["taxonomicId"],
                albumDir.joinpath(row["albumName"]),
                thumbDir.joinpath(row["thumbName"]),
                QDateTime.fromString(row["shootTime"], "yyyy-MM-dd HH:mm:ss"),
                row["isMovie"],
            )
            albumInfoList.append(albumInfo)
        albumData = AlbumData(taxonomicItem, thumbPic, albumInfoList)
        return albumData

    def AddMedia(self, para: tuple[AlbumData, list[Path]]):
        albumData = para[0]
        pathList = para[1]
        taxonomicid = albumData.taxonomicItem.id
        thumbDir = self.workPath.joinpath("img/thumb").joinpath(
            albumData.taxonomicItem.name
        )
        albumDir = self.workPath.joinpath("img/album").joinpath(
            albumData.taxonomicItem.name
        )
        albumThumbPath = self.workPath.joinpath("img/thumb").joinpath(
            f"{albumData.taxonomicItem.name}.jpg"
        )
        thumbDir.mkdir(parents=True, exist_ok=True)
        albumDir.mkdir(parents=True, exist_ok=True)
        count = 0
        for path in pathList:
            extension = path.suffix.lower()
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            thumbName = f"{path.stem}_{timestamp}.jpg"
            albumName = f"{path.stem}_{timestamp}{path.suffix}"
            thumbPath = str(thumbDir.joinpath(thumbName))
            albumPath = str(albumDir.joinpath(albumName))
            if extension == ".jpg":
                try:
                    exifData = piexif.load(str(path))
                    bdateTime = exifData["Exif"][piexif.ExifIFD.DateTimeOriginal]
                    sdateTime = bdateTime.decode("utf-8")
                    qDateTime = QDateTime.fromString(sdateTime, "yyyy:MM:dd HH:mm:ss")
                except:
                    qDateTime = QDateTime.fromSecsSinceEpoch(int(path.stat().st_ctime))
                shootTime = qDateTime.toString("yyyy-MM-dd HH:mm:ss")
                try:
                    thumb = QPixmap(path).scaled(
                        QSize(600, 600),
                        Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                        Qt.TransformationMode.SmoothTransformation,
                    )
                    thumb = thumb.copy(
                        (thumb.size().width() - 600) / 2,
                        (thumb.size().height() - 600) / 2,
                        600,
                        600,
                    )

                    thumb.save(thumbPath)
                    if not albumThumbPath.exists():
                        thumb.save(str(albumThumbPath))
                    thumb

                    shutil.move(path, albumPath)
                    sql = """
                        INSERT INTO [media]
                                ([taxonomicId]
                                ,[albumName]
                                ,[thumbName]
                                ,[shootTime]
                                ,[isMovie])
                            VALUES
                                (?,?,?,?,?)
                    """
                    data = (taxonomicid, albumName, thumbName, shootTime, False)
                    self.cur.execute(sql, data)
                    self.conn.commit()
                    count = count + 1
                except Exception as e:
                    print(e)
                    continue
            elif extension == ".mov" or extension == ".mp4":
                qDateTime = QDateTime.fromSecsSinceEpoch(int(path.stat().st_ctime))
                shootTime = qDateTime.toString("yyyy-MM-dd HH:mm:ss")
                try:
                    clip = VideoFileClip(str(path))
                    frame: numpy.ndarray = clip.get_frame(0)
                    image = QImage(
                        frame.data,
                        frame.shape[1],
                        frame.shape[0],
                        QImage.Format.Format_RGB888,
                    )
                    thumb = QPixmap.fromImage(image).scaled(
                        QSize(600, 600),
                        Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                        Qt.TransformationMode.SmoothTransformation,
                    )
                    thumb = thumb.copy(
                        (thumb.size().width() - 600) / 2,
                        (thumb.size().height() - 600) / 2,
                        600,
                        600,
                    )
                    thumb.save(thumbPath)
                    if not albumThumbPath.exists():
                        thumb.save(str(albumThumbPath))
                    clip.close()
                    shutil.move(path, albumPath)
                    sql = """
                        INSERT INTO [media]
                                ([taxonomicId]
                                ,[albumName]
                                ,[thumbName]
                                ,[shootTime]
                                ,[isMovie])
                            VALUES
                                (?,?,?,?,?)
                    """
                    data = (taxonomicid, albumName, thumbName, shootTime, True)
                    self.cur.execute(sql, data)
                    self.conn.commit()
                    count = count + 1
                except Exception as e:
                    print(e)
                    continue
        return count
