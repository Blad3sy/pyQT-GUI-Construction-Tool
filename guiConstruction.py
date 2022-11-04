from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

class Application(QApplication):

    def __init__(self):
        super().__init__(sys.argv)
    
class Window(QMainWindow):
    
    def __init__(self, title, width, height):
        super().__init__()

        self.xPos = 200
        self.yPos = 200
        self.width = width
        self.height = height
        self.title = title

        self.setGeometry(self.xPos, self.yPos, self.width, self.height)
        self.setWindowTitle(self.title)

        self.show()
    
    def setTheCentralWidget(self, object):
        self.setCentralWidget(object)
        
class Layout(QWidget):

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        parent.setTheCentralWidget(self)

        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setAlignment(Qt.AlignTop)
    
    def toAddWidget(self, object):
        self.mainLayout.addWidget(object)

class Label(QLabel):
    
    def __init__(self, parent, text):
        super().__init__()
        
        parent.toAddWidget(self)
        self.text = text

        self.setText(self.text)

        self.show()

class Image(QLabel):

    def __init__(self, parent, image):
        super().__init__()

        parent.toAddWidget(self)
        self.image = image

        self.setPixmap(QPixmap(image))

        self.show()

class Button(QPushButton):

    def __init__(self, parent, command, text):
        super().__init__()
        
        parent.toAddWidget(self)
        self.text = text

        self.clicked.connect(command)
        self.setText(self.text)

        self.show()