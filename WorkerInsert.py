import sqlite3
from Worker import Worker
from pathlib import Path
from GlobalType import TaxonomicItem, TaxonomicTree, TaxonomicPath
import requests
from PySide6.QtWidgets import QMessageBox


class WorkerInsert(Worker):
    def __init__(self, workPath: Path) -> None:
        self.workPath = workPath
        self.dbPath = self.workPath.joinpath("db/database.db")
        super().__init__()

    def setup(self):
        self.conn = sqlite3.connect(self.dbPath)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        return super().setup()

    def GetTaxonomicPathFromDB(self, name: str) -> TaxonomicPath:
        sql = """
            WITH RECURSIVE [taxonomic_path]
            AS (
                SELECT [id]
                    ,[parentId]
                    ,[name]
                    ,[rank]
                FROM [taxonomic]
                WHERE [name] = ?
                    AND [rank] = 'Species'
                UNION ALL
                SELECT [t].[id]
                    ,[t].[parentId]
                    ,[t].[name]
                    ,[t].[rank]
                FROM [taxonomic] [t]
                JOIN [taxonomic_path] [tp] ON [t].[id] = [tp].[parentId]
            )
            SELECT [name],[rank] FROM [taxonomic_path]
        """
        data = (name,)
        taxonomicPath = TaxonomicPath()
        self.cur.execute(sql, data)
        rows = self.cur.fetchall()
        for row in rows:
            if row["rank"] == "Kingdom":
                taxonomicPath.Kingdom = row["name"]
            elif row["rank"] == "Phylum":
                taxonomicPath.Phylum = row["name"]
            elif row["rank"] == "Class":
                taxonomicPath.Class = row["name"]
            elif row["rank"] == "Order":
                taxonomicPath.Order = row["name"]
            elif row["rank"] == "Family":
                taxonomicPath.Family = row["name"]
            elif row["rank"] == "Genus":
                taxonomicPath.Genus = row["name"]
            elif row["rank"] == "Species":
                taxonomicPath.Species = row["name"]

        taxonomicPath.Status = "accepted"
        return taxonomicPath

    def GetTaxonomicPathFromWoRMS(self, name: str) -> TaxonomicPath:
        # url = f"https://www.marinespecies.org/rest/AphiaRecordsByName/{name}?like=true&marine_only=true&offset=1"
        url = f"https://www.marinespecies.org/rest/AphiaRecordsByNames?scientificnames%5B%5D={name}&like=true&marine_only=true"
        taxonomicPath = TaxonomicPath()
        try:
            response = requests.get(url)
            data = response.json()
            data = data[0][0]
            taxonomicPath.Kingdom = data.get("kingdom", "")
            taxonomicPath.Phylum = data.get("phylum", "")
            taxonomicPath.Class = data.get("class", "")
            taxonomicPath.Order = data.get("order", "")
            taxonomicPath.Family = data.get("family", "")
            taxonomicPath.Genus = data.get("genus", "")
            taxonomicPath.Species = data.get("scientificname", "")
            taxonomicPath.Status = data.get("status", "")
        except:
            pass
        return taxonomicPath

    def GetTaxonomicPathFromGBIF(self, name: str) -> TaxonomicPath:
        url = f"https://api.gbif.org/v1/species/match?name={name}"
        taxonomicPath = TaxonomicPath()
        try:
            response = requests.get(url)
            data = response.json()
            taxonomicPath.Kingdom = data.get("kingdom", "")
            taxonomicPath.Phylum = data.get("phylum", "")
            taxonomicPath.Class = data.get("class", "")
            taxonomicPath.Order = data.get("order", "")
            taxonomicPath.Family = data.get("family", "")
            taxonomicPath.Genus = data.get("genus", "")
            taxonomicPath.Species = data.get("species", "")
            taxonomicPath.Status = "accepted"
        except Exception as e:
            pass
        return taxonomicPath

    def InsertTaxonomicPath(self, taxonomicPath: TaxonomicPath) -> int:
        paraTuple = (
            ("Kingdom", taxonomicPath.Kingdom),
            ("Phylum", taxonomicPath.Phylum),
            ("Class", taxonomicPath.Class),
            ("Order", taxonomicPath.Order),
            ("Family", taxonomicPath.Family),
            ("Genus", taxonomicPath.Genus),
            ("Species", taxonomicPath.Species),
        )
        parentId = 1
        for para in paraTuple:
            sql = "SELECT [id] FROM [taxonomic] WHERE name = ? and parentId = ? and rank = ?"
            data = (para[1], parentId, para[0])
            self.cur.execute(sql, data)
            rows = self.cur.fetchall()
            if rows:
                parentId = rows[0]["id"]
            else:
                sql = "INSERT INTO [taxonomic]([name],[parentId],[rank],[commonName],[otherNames],[information]) VALUES (?,?,?,'','','')"
                data = (para[1], parentId, para[0])
                self.cur.execute(sql, data)
                sql = "SELECT last_insert_rowid() as id"
                self.cur.execute(sql)
                self.conn.commit()
                parentId = self.cur.fetchone()["id"]
        return parentId
