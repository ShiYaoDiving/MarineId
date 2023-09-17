from PySide6.QtCore import QDateTime, QEvent
import re
from PySide6.QtGui import QPixmap
from pathlib import Path


class CallbackEvent(QEvent):
    def __init__(self, callback: callable, para):
        super().__init__(QEvent.Type.User)
        self.callback = callback
        self.para = para


class DiveLog:
    def __init__(
        self,
        id: int = -1,
        timeIn: QDateTime = QDateTime(1990, 10, 1, 0, 0, 0),
        timeOut: QDateTime = QDateTime(1990, 10, 1, 0, 0, 0),
        location: str = "",
        diveSite: str = "",
    ):
        self.id = id
        self.timeIn = timeIn
        self.timeOut = timeOut
        self.location = location
        self.diveSite = diveSite

    def GetLocationList(diveLogList: list) -> list[str]:
        return sorted(list(set([diveLog.location for diveLog in diveLogList])))

    def GetDiveSiteListByLocation(diveLogList: list, location: str) -> list[str]:
        return sorted(
            list(
                set(
                    [
                        diveLog.diveSite
                        for diveLog in diveLogList
                        if diveLog.location == location
                    ]
                )
            )
        )


class TaxonomicItem:
    def __init__(
        self,
        id: int = 0,
        parentId: int = 0,
        name: str = "",
        rank: str = "",
        commonName: str = "",
        otherNames: str = "",
        information: str = "",
    ):
        self.id = id
        self.parentId = parentId
        self.name = name
        self.rank = rank
        self.commonName = commonName
        self.otherNames = otherNames
        self.information = information


class TaxonomicPath:
    def __init__(
        self,
        Kingdom="",
        Phylum="",
        Class="",
        Order="",
        Family="",
        Genus="",
        Species="",
        Status="",
    ):
        self.Kingdom = Kingdom
        self.Phylum = Phylum
        self.Class = Class
        self.Order = Order
        self.Family = Family
        self.Genus = Genus
        self.Species = Species
        self.Status = Status

    def NoBlankField(self) -> bool:
        return (
            self.Kingdom != ""
            and self.Phylum != ""
            and self.Class != ""
            and self.Order != ""
            and self.Family != ""
            and self.Genus != ""
            and self.Species != ""
        )


class TaxonomicTree:
    def __init__(self, taxonomicItemList: list[TaxonomicItem] = []):
        self.itemDict: dict[int, TaxonomicItem] = {}
        for taxonomicItem in taxonomicItemList:
            self.itemDict[taxonomicItem.id] = taxonomicItem

    def GetNodesByKeyword(self, keyword: str) -> list[TaxonomicItem]:
        taxonomicItemList = []
        for taxonomicItem in self.itemDict.values():
            if (
                (re.search(keyword, taxonomicItem.name) is not None)
                or (re.search(keyword, taxonomicItem.commonName) is not None)
                or (re.search(keyword, taxonomicItem.otherNames) is not None)
                or (re.search(keyword, taxonomicItem.information) is not None)
            ):
                taxonomicItemList.append(taxonomicItem)
        return taxonomicItemList

    def GetNodeById(self, id: int) -> TaxonomicItem:
        return self.itemDict[id]

    def GetChildNodesById(self, id: int) -> list[TaxonomicItem]:
        return [
            taxonomicItem
            for taxonomicItem in self.itemDict.values()
            if (taxonomicItem.parentId == id)
        ]

    def GetLeafNodesById(self, id: int) -> list[TaxonomicItem]:
        if self.itemDict[id].rank == "Species":
            return [self.itemDict[id]]
        taxonomicItemList = []
        for child in self.GetChildNodesById(id):
            taxonomicItemList.extend(self.GetLeafNodesById(child.id))
        return taxonomicItemList

    def GetParentNodeById(self, id: int) -> TaxonomicItem:
        if self.itemDict[id].parentId <= 0:
            return None
        else:
            return self.itemDict[self.itemDict[id].parentId]

    def GetAncestorNodesById(self, id: int) -> list[TaxonomicItem]:
        if self.itemDict[id].parentId == 0:
            return []
        parentTaxonomicItem = self.GetParentNodeById(id)
        taxonomicItemList = [parentTaxonomicItem]
        taxonomicItemList.extend(self.GetAncestorNodesById(self.itemDict[id].parentId))
        return taxonomicItemList

    def GetNodesByName(self, name: str) -> list[TaxonomicItem]:
        taxonomicItemList = []
        for taxonomicItem in self.itemDict.values():
            if taxonomicItem.name == name:
                taxonomicItemList.append(taxonomicItem)
        return taxonomicItemList


class AlbumInfo:
    def __init__(
        self,
        id: int,
        taxonomicId: int,
        albumPath: Path,
        thumbPath: Path,
        shootTime: QDateTime,
        isMovie: bool,
    ) -> None:
        self.id = id
        self.taxonomicId = taxonomicId
        self.albumPath = albumPath
        self.thumbPath = thumbPath
        self.shootTime = shootTime
        self.isMovie = isMovie
        pass


class AlbumData:
    def __init__(
        self,
        taxonomicItem: TaxonomicItem,
        thumbPic: QPixmap,
        albumInfoList: list[AlbumInfo],
    ) -> None:
        self.taxonomicItem = taxonomicItem
        self.thumbPic = thumbPic
        self.albumInfoList = albumInfoList
        pass
