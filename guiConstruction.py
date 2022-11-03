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
        self.width = 600
        self.height = 600
        self.title = "Test"

        self.setGeometry(self.xPos, self.yPos, self.width, self.height)
        self.setWindowTitle(self.title)

        self.show()

class Label(QLabel):
    
    def __init__(self, parent, text, xPos, yPos):
        QLabel.__init__(self, parent)

        self.xPos = xPos
        self.yPos = yPos
        self.width = None
        self.height = None
        self.text = text

        self.move(self.xPos, self.yPos)
        self.setText(self.text)

        self.show()