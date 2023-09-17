import sqlite3
from Worker import Worker
from pathlib import Path
from GlobalType import TaxonomicItem, TaxonomicTree
from bs4 import BeautifulSoup
import requests
from pathlib import Path
import shutil
import re
import opencc


class WorkerUpdate(Worker):
    def __init__(self, workPath: Path) -> None:
        self.workPath = workPath
        self.dbPath = self.workPath.joinpath("db/database.db")
        super().__init__()

    def setup(self):
        self.conn = sqlite3.connect(self.dbPath)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        return super().setup()

    def GetTaxonomicItem(self, id: int) -> TaxonomicItem:
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
        return taxonomicItem

    def UpdateTaxonomicItem(self, taxonomicItem: TaxonomicItem) -> int:
        sql = """
            UPDATE [taxonomic]
                SET [name] = ?
                    ,[parentId] = ?
                    ,[rank] = ?
                    ,[commonName] = ?
                    ,[otherNames] = ?
                    ,[information] = ?
                WHERE [id] = ?
        """
        data = (
            taxonomicItem.name,
            taxonomicItem.parentId,
            taxonomicItem.rank,
            taxonomicItem.commonName,
            taxonomicItem.otherNames,
            taxonomicItem.information,
            taxonomicItem.id,
        )
        self.cur.execute(sql, data)
        self.conn.commit()
        return taxonomicItem.id

    def DeleteTaxonomicItem(self, id: int) -> int:
        sql = "SELECT [parentId] FROM [taxonomic] WHERE [id] = ?"
        data = (id,)
        self.cur.execute(sql, data)
        parentId = self.cur.fetchone()["parentId"]
        sql = "DELETE FROM [taxonomic] WHERE [id] = ?"
        data = (id,)
        self.cur.execute(sql, data)
        self.conn.commit()
        return parentId

    def GetCommonNameFromAquaml(self, name: str) -> str:
        url = "https://aquaml.com/s/" + name.replace(" ", "_") + ".html"
        try:
            html = requests.get(url)
            html.encoding = "utf-8"
            soup = BeautifulSoup(html.text, "lxml")
            commonName = soup.select("#sec-name").pop().getText()
        except Exception as e:
            commonName = ""
        return commonName

    def GetCommonNameFromTaiEOL(self, name: str) -> str:
        url = (
            "https://taieol.tw/index.php?q=classify-jstree-ajax/autocomplete/muse_taicol/1/"
            + name
        )
        try:
            response = requests.get(url)
            data: dict = response.json()
            result = list(data.values())[-1]
            pattern = r"＜(.*?)＞"
            matches = re.findall(pattern, result)
            if matches:
                commonName = matches[0]
                commonName = opencc.OpenCC("t2s").convert(commonName)
            else:
                commonName = ""
        except Exception as e:
            commonName = ""
        return commonName
