#!/usr/bin/env python

import os
import random
import sys
import QTermWidget
from email.message import EmailMessage

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QGridLayout, QLineEdit, QComboBox, QLabel


class Composer(QWidget):

    def __init__(self):
        super().__init__()
        self.lefrom = None
        self.s_to = ''
        self.s_cc = ''
        self.s_bcc = ''
        self.s_subject = ''
        # TODO: import tempfile benutzen
        self.tempfilepath = str(random.getrandbits(128))
        self.initUI()

    @pyqtSlot()
    def sendOrDiscard(self):
        print(self.tempfilepath)
        try:
            file = open(self.tempfilepath, 'r')
        except:
            # Discard
            print("Datei net da")
        else:
            # Send
            print("Datei da")
            print(self.lefrom.currentText())
            print(self.s_to)
            print(self.s_cc)
            print(self.s_bcc)
            mail = EmailMessage()
            mail.set_content(file.read())
            mail['From'] = self.lefrom.currentText()
            mail['To'] = self.s_to
            mail['CC'] = self.s_cc
            mail['BCC'] = self.s_bcc
            print(mail)
            file.close()
            os.remove(self.tempfilepath)
        self.close()

    @pyqtSlot(str)
    def updateTo(self, to):
        self.s_to = to

    @pyqtSlot(str)
    def updateCC(self, cc):
        self.s_cc = cc

    @pyqtSlot(str)
    def updateBCC(self, bcc):
        self.s_bcc = bcc

    @pyqtSlot(str)
    def updateSubject(self, subject):
        self.s_subject = subject

    @pyqtSlot(str)
    def executeTerminal(self, subject):
        self.textedit.execute()

    def initUI(self):
        layout = QVBoxLayout()
        upperlayout = QGridLayout()
        terminalfont = QFont('Monospace', 12)

        self.lefrom = QComboBox()
        leto = QLineEdit()
        lecc = QLineEdit()
        lebcc = QLineEdit()
        lesubject = QLineEdit()
        labfrom = QLabel('From')
        labto = QLabel('To')
        labcc = QLabel('CC')
        labbcc = QLabel('BCC')
        labsubject = QLabel('Subject')

        self.lefrom.addItem("Account 1")
        self.lefrom.addItem("Account 2")

        leto.textChanged.connect(self.updateTo)
        lecc.textChanged.connect(self.updateCC)
        lebcc.textChanged.connect(self.updateBCC)
        lesubject.textChanged.connect(self.updateSubject)

        # Initializing QTermWidget, but not starting it right away
        textedit = QTermWidget.QTermWidget(0)
        textedit.setColorScheme('Linux')
        textedit.setTerminalFont(terminalfont)
        textedit.finished.connect(self.sendOrDiscard)
        # Reconfiguring shell to $EDITOR
        textedit.setShellProgram('/usr/bin/vim')
        textedit.setArgs([self.tempfilepath])
        textedit.startShellProgram()

        upperlayout.addWidget(labfrom, 0, 0)
        upperlayout.addWidget(self.lefrom, 0, 1)
        upperlayout.addWidget(labto, 1, 0)
        upperlayout.addWidget(leto, 1, 1)
        upperlayout.addWidget(labcc, 2, 0)
        upperlayout.addWidget(lecc, 2, 1)
        upperlayout.addWidget(labbcc, 3, 0)
        upperlayout.addWidget(lebcc, 3, 1)
        upperlayout.addWidget(labsubject, 4, 0)
        upperlayout.addWidget(lesubject, 4, 1)
        layout.addLayout(upperlayout)
        layout.addWidget(textedit)

        self.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    composer = Composer()
    sys.exit(app.exec_())
