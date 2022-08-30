# -*- coding: utf-8 -*-

"""
Py40 PyQt5 tutorial
This example shows three labels on a window
using absolute positioning.
author: Jan Bodnar
website: py40.com
last edited: January 2015
"""

import sys
import os
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit
import subprocess


class GitHelperMainW(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        #创建一个水平布局
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
        cmd1 = "git add . "
        cmd2 = "git commit -m \"auto commit\""
        os.system(cmd1)
        self.logEdit.setText(self.logEdit.toPlainText() + "\n" + cmd1)
        os.system(cmd2)
        self.logEdit.setText(self.logEdit.toPlainText() + "\n" + cmd2)
        cmd3 = "git push origin {}".format(self.branchEdit.text())
        p = subprocess.Popen(cmd3, shell=False,stdout=subprocess.PIPE,encoding="utf-8")
        self.logEdit.setText(self.logEdit.toPlainText() + "\n" + cmd3)
        out,err = p.communicate()
        for line in out.splitlines():
            self.logEdit.setText(self.logEdit.toPlainText() + "\n" + line)

    def onPullButton(self):
        cmd = "git pull origin {}".format(self.branchEdit.text())
        p = subprocess.Popen(cmd, shell=False,stdout=subprocess.PIPE,encoding="utf-8")
        self.logEdit.setText(self.logEdit.toPlainText() + "\n" + cmd)
        out,err = p.communicate()
        for line in out.splitlines():
            self.logEdit.setText(self.logEdit.toPlainText() + "\n" + line)

    def onConfigButton(self):
        os.system("git config  user.email \"{}\"".format(self.emailEdit.text()))
        os.system("git config  user.name \"{}\"".format(self.userEdit.text()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GitHelperMainW()
    sys.exit(app.exec_())
    input("please input any key to exit!")