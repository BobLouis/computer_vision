import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,QPushButton)
from PyQt5.QtGui import QFont

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('hello world')
        self.setGeometry(50, 50, 200, 150)
        self.mylabel = QLabel('hello world', self)
        self.mylabel.move(40, 50)
        self.mylabel.setFont(QFont('Arial', 18))
        
        self.mybutton = QPushButton('button', self)
        self.mybutton.move(40, 20)
        self.mybutton.clicked.connect(self.onButtonClick)
    
    def onButtonClick(self):
        self.mybutton.setText('hello wolrd')


if __name__ == '__main__':
    print(__name__)
    app = QApplication(sys.argv)
    w = MyWidget()
    w.show()
    sys.exit(app.exec_())