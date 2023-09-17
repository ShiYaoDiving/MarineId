from queue import Queue
from PySide6.QtCore import QThread, QObject, Qt
from PySide6.QtWidgets import QApplication

from GlobalType import CallbackEvent


class WorkerTask:
    def __init__(
        self,
        func: callable,
        para: any = None,
        callback: callable = None,
        reciever: QObject = None,
    ):
        self.func = func
        self.para = para
        self.callback = callback
        self.reciever = reciever


class Worker(QThread):
    def __init__(self) -> None:
        super().__init__()
        self.queue = Queue()
        self.running = True
        self.start()

    def add(
        self,
        func: callable,
        para: any = None,
        callback: callable = None,
        reciever: QObject = None,
        changeCursor: bool = True,
    ):
        task = WorkerTask(func, para, callback, reciever)
        if task.reciever == None:
            task.reciever = self.parent()
        self.queue.put(task)
        if changeCursor:
            QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)

    def stop(self):
        while not self.queue.empty():
            self.queue.get()
        self.queue.put(WorkerTask(self.task_Exit))

    def setup(self):
        self.running = True
        pass

    def run(self):
        self.setup()
        while self.running:
            task: WorkerTask = self.queue.get()

            ret = task.func(task.para)
            if task.callback != None:
                QApplication.instance().postEvent(
                    task.reciever, CallbackEvent(task.callback, ret)
                )

    def task_Exit(self, para=None):
        self.running = False
