import sqlite3
from Worker import Worker
from pathlib import Path
from GlobalType import TaxonomicItem, TaxonomicTree


class WorkerSearch(Worker):
    def __init__(self, workPath: Path) -> None:
        self.workPath = workPath
        self.dbPath = self.workPath.joinpath("db/database.db")
        super().__init__()

    def setup(self):
        self.conn = sqlite3.connect(self.dbPath)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        return super().setup()

    def SearchTaxonomic(self, keyword) -> list[TaxonomicItem]:
        sql = """
            SELECT [id]
                ,[name]
                ,[parentId]
                ,[rank]
                ,[commonName]
                ,[otherNames]
                ,[information]
            FROM [taxonomic]
            WHERE [name] LIKE ?
                OR [commonName] LIKE ?
                OR [otherNames] LIKE ?
        """
        taxonomicItemList: list[TaxonomicItem] = []
        data = (
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%",
        )
        self.cur.execute(sql, data)
        rows = self.cur.fetchall()
        for row in rows:
            taxonomicItem = TaxonomicItem(
                int(row["id"]),
                int(row["parentId"]),
                str(row["name"]),
                str(row["rank"]),
                str(row["commonName"]),
                str(row["otherNames"]),
                str(row["information"]),
            )
            taxonomicItemList.append(taxonomicItem)
        return taxonomicItemList
