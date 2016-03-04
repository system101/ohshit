#!/usr/bin/env python

import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.wtf = QImage("images/yukkuri-15.jpg")
        self.rabbit = QImage("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        q = QPainter()
        p.begin(self)
        p.drawImage(QRect(200, 100, 320, 320), self.rabbit)
        p.end()
        q.begin(self)
        q.drawImage(QRect(200+150, 100+150, 320+150, 320+150), self.wtf)
        q.end()
def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
