from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

class Application(QApplication):

    def __init__(self):
        super().__init__(sys.argv)
    
class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.xPos = 200
        self.yPos = 200
        self.width = 300
        self.height = 300
        self.title = "Test"

        self.setGeometry(self.xPos, self.yPos, self.width, self.height)
        self.setWindowTitle(self.title)

class Label(QLabel):
    def __init__(self):
        super().__init__()

        self.xPos = 100
        self.yPos = 100
        self.width = None
        self.height = None
        self.text = "Test"

        self.move(self.xPos, self.yPos)