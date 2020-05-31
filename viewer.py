#!/usr/bin/env python

from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QTextEdit
from PyQt5.QtGui import QFont
#from PyQt5.QtCore import Qt, pyqtSlot

import sys

class Viewer(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(0)
        font = QFont("Monospace", 12)
        textview = QTextEdit()
        textview.setReadOnly(True)
        textview.setFont(font)
        textview.setHtml("<b>test</b>test")
        #textview.setPlainText("<b>test</b>test")

        layout.addWidget(textview)

        self.setLayout(layout)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = Viewer()
    sys.exit(app.exec_())