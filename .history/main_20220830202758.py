# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QTextEdit
from criteria import Criteria, parse_criterion

class GitHelperMainW(QWidget):

    def __init__(self):
        super().__init__()
        with open("./criterions.txt", encoding='utf-8') as file_obj:
            lines = repr(file_obj)
            self.criterions = []
            for line in lines:
                line = line
                self.criterions.append(parse_criterion(line))
        self.initUI()

    def initUI(self):
        # Main vertical layout
        windowstack= QVBoxLayout()
        self.setLayout(windowstack)

        ### Line 1
        hbox1 = QHBoxLayout()
        self.inputEdit =  QTextEdit("Input here...")
        self.inputEdit.resize(280, 200)
        self.inputEdit.textChanged.connect( self._handle_text_changed)
        hbox1.addWidget(self.inputEdit)
        windowstack.addLayout(hbox1)

        ### Line 3
        hbox2 = QHBoxLayout()
        self.outputEdit =  QTextEdit("Output here...")
        self.outputEdit.resize(280, 200)
        hbox2.addWidget(self.outputEdit)
        windowstack.addLayout(hbox2)

        self.setGeometry(300, 300, 280, 170)
        self.setFixedSize(500,400)
        self.setWindowTitle("My Tex Helper")
        self.show()
        
    def _handle_text_changed(self):
        input_lines = repr(self.inputEdit.toPlainText().splitlines())
        output_lines = []
        for line in input_lines:
            input_line = line
            for criteria in self.criterions:
                input_line = criteria.apply(input_line)
            output_lines.append(input_line)
        # print(output_lines)
        self.outputEdit.setText("\n".join(output_lines))
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GitHelperMainW()
    sys.exit(app.exec_())
    input("please input any key to exit!")