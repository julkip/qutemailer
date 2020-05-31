#!/usr/bin/env python

from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QHBoxLayout, QTreeView, QTextEdit
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt
from imaplib import IMAP4_SSL

import sys

from account import Account


class Mainwindow(QWidget):

    FROM, SUBJECT, DATE = range(3)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()
        secondlayout = QVBoxLayout()

        templist = QTextEdit()

        maillist = QTreeView()
        maillist.setRootIsDecorated(False)
        maillist.setAlternatingRowColors(True)

        model = self.create_mail_model()
        maillist.setModel(model)
        self.add_mail(model, 'service@github.com', 'Your Github Donation', '03/25/2017 02:05 PM')
        self.add_mail(model, 'support@github.com', 'Github Projects', '02/02/2017 03:05 PM')
        self.add_mail(model, 'service@phone.com', 'Your Phone Bill', '01/01/2017 04:05 PM')

        tempview = QTextEdit()

        secondlayout.addWidget(maillist)
        secondlayout.addWidget(tempview)
        layout.addWidget(templist)
        layout.addLayout(secondlayout)

        self.setLayout(layout)
        self.show()

    def create_mail_model(self):
        model = QStandardItemModel(0, 3)
        model.setHeaderData(self.FROM, Qt.Horizontal, 'From')
        model.setHeaderData(self.SUBJECT, Qt.Horizontal, "Subject")
        model.setHeaderData(self.DATE, Qt.Horizontal, "Date")
        return model

    def add_mail(self, model, mail_from, subject, date):
        model.insertRow(0)
        model.setData(model.index(0, self.FROM), mail_from)
        model.setData(model.index(0, self.SUBJECT), subject)
        model.setData(model.index(0, self.DATE), date)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow()
    sys.exit(app.exec_())
