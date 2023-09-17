import sqlite3
from Worker import Worker
from pathlib import Path
from GlobalType import DiveLog
from PySide6.QtCore import QDateTime


class WorkerDiveLog(Worker):
    def __init__(self, workPath: Path) -> None:
        self.workPath = workPath
        self.dbPath = self.workPath.joinpath("db/database.db")
        super().__init__()

    def setup(self):
        self.conn = sqlite3.connect(self.dbPath)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        return super().setup()

    def GetDiveLogList(self, para) -> list[DiveLog]:
        sql = """
            SELECT [id]
                ,strftime('%Y-%m-%d %H:%M', timeIn) AS [timeIn]
                ,strftime('%Y-%m-%d %H:%M', timeOut) AS [timeOut]
                ,[location]
                ,[diveSite]
            FROM [dive_log]
            ORDER BY [timeIn] DESC
        """
        self.cur.execute(sql)
        rows = self.cur.fetchall()
        diveLogList = []
        for row in rows:
            diveLog = DiveLog()
            try:
                diveLog.id = row["id"]
                diveLog.timeIn = QDateTime.fromString(row["timeIn"], "yyyy-MM-dd HH:mm")
                diveLog.timeOut = QDateTime.fromString(
                    row["timeOut"], "yyyy-MM-dd HH:mm"
                )
                diveLog.location = row["location"]
                diveLog.diveSite = row["diveSite"]
                diveLogList.append(diveLog)
            except Exception as e:
                print(e)
        return diveLogList

    def InsertDiveLog(self, diveLog: DiveLog) -> int:
        sql = """
        INSERT INTO [dive_log] (
	        [timeIn]
	        ,[timeOut]
	        ,[location]
	        ,[diveSite]
	        )
        VALUES (?,?,?,?)
        """
        data = (
            diveLog.timeIn.toString("yyyy-MM-dd HH:mm"),
            diveLog.timeOut.toString("yyyy-MM-dd HH:mm"),
            diveLog.location,
            diveLog.diveSite,
        )
        self.cur.execute(sql, data)
        self.conn.commit()
        sql = "SELECT last_insert_rowid() as id"
        self.cur.execute(sql)
        return self.cur.fetchone()["id"]

    def DeleteDiveLog(self, id):
        sql = """DELETE FROM [dive_log] WHERE id=?"""
        data = (id,)
        self.cur.execute(sql, data)
        self.conn.commit()
