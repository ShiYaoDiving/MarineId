import sqlite3
from Worker import Worker
from pathlib import Path
from GlobalType import TaxonomicItem, TaxonomicTree
import time


class WorkerGallery(Worker):
    def __init__(self, workPath: Path) -> None:
        self.workPath = workPath
        self.dbPath = self.workPath.joinpath("db/database.db")
        super().__init__()

    def setup(self):
        self.conn = sqlite3.connect(self.dbPath)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        return super().setup()

    def GetTaxonomicItemList(self, idList: list[int]):
        sql = """
            SELECT [id]
                ,[parentId]
                ,[name]
                ,[rank]
                ,[commonName]
                ,[otherNames]
                ,[information]
            FROM [taxonomic]
        """
        taxonomicItemList: list[TaxonomicItem] = []
        self.cur.execute(sql)
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
        taxonomicTree = TaxonomicTree(taxonomicItemList)
        taxonomicItemSet: set[TaxonomicItem] = set()

        for id in idList:
            taxonomicItemSet.update(taxonomicTree.GetLeafNodesById(id))
        taxonomicItemList = list(taxonomicItemSet)
        taxonomicItemList = sorted(taxonomicItemList, key=lambda x: x.id)
        return taxonomicItemList
