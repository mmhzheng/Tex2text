# -*- coding: utf-8 -*-

import sys
import os
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit
import subprocess


class GitHelperMainW(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # vertical layout
        windowstack= QVBoxLayout()
        self.setLayout(windowstack)

        ### Line 1
        hbox1 = QHBoxLayout()
        self.pushButton = QPushButton("Push")
        self.pushButton.clicked.connect(self.onPushButton)
        self.pullButton = QPushButton("Pull")
        self.pullButton.clicked.connect(self.onPullButton)
        branchLabel= QLabel("Branch")
        self.branchEdit = QLineEdit("master")
        hbox1.addWidget(branchLabel)
        hbox1.addWidget(self.branchEdit)
        hbox1.addWidget(self.pushButton)
        hbox1.addWidget(self.pullButton)
        windowstack.addLayout(hbox1)

        ### Line 2
        hbox2 = QHBoxLayout()
        emailLabel= QLabel("Email")
        self.emailEdit = QLineEdit("your email")
        userLabel= QLabel("Username")
        self.userEdit = QLineEdit("your name")
        self.configButton = QPushButton("Config")
        self.configButton.clicked.connect(self.onConfigButton)
        hbox2.addWidget(emailLabel)
        hbox2.addWidget(self.emailEdit)
        hbox2.addWidget(userLabel)
        hbox2.addWidget(self.userEdit)
        hbox2.addWidget(self.configButton)
        windowstack.addLayout(hbox2)

        ### Line 3
        hbox3 = QHBoxLayout()
        self.logEdit =  QTextEdit("logs here...")
        self.logEdit.resize(280, 200)
        hbox3.addWidget(self.logEdit)
        windowstack.addLayout(hbox3)

        self.setGeometry(300, 300, 280, 170)
        self.setFixedSize(500,400)
        self.setWindowTitle('My Git Helper')
        self.show()

    def onPushButton(self):
        pass

    def onPullButton(self):
        pass

    def onConfigButton(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GitHelperMainW()
    sys.exit(app.exec_())
    input("please input any key to exit!")