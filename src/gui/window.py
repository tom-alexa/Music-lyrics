
# src  →  gui  →  window.py

from pathlib import PurePath
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Music lyrics"
        self.icon_path = "src/gui/img/microphone.png"
        self.left = 400
        self.top = 200
        self.w_width = 1000
        self.w_height = 600

        self.init_window()


    def init_window(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(str(PurePath(self.icon_path))))
        self.setGeometry(self.left, self.top, self.w_width, self.w_height)

        self.show()
