# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit

class GitHelperMainW(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Main vertical layout
        windowstack= QVBoxLayout()
        self.setLayout(windowstack)

        ### Line 1
        hbox1 = QHBoxLayout()
        self.inputEdit =  QTextEdit("Input here...")
        self.inputEdit.resize(280, 200)
        hbox3.addWidget(self.logEdit)
        windowstack.addLayout(hbox3)

        ### Line 3
        hbox3 = QHBoxLayout()
        self.logEdit =  QTextEdit("Output here...")
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