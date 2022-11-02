from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class Window():
    
    def __init__(self):
        self.xPos = None
        self.yPos = None
        self.width = None
        self.height = None
        self.title = None

    def windowStart(self):
        app = QApplication(sys.argv)
        win = QMainWindow()
    
        win.setGeometry(self.xPos, self.yPos, self.width, self.height)
        win.setWindowTitle(self.title)

        win.show()
        sys.exit(app.exec_())