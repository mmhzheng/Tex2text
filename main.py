# -*- coding: utf-8 -*-

from datetime import datetime
import sys
import os
from PyQt5.QtWidgets import *
from matplotlib.pyplot import table
from numpy import mat
from criteria import parse_criterion_v1, parse_criterion_v2

CONFIG_ROW = 50

class GitHelperMainW(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Main vertical layout

        window_layout = QVBoxLayout()

        # Menu Row
        menuStack = QHBoxLayout()        
        self.loadButton = QPushButton("Load")
        self.saveButton = QPushButton("Save")
        self.loadButton.clicked.connect(self._handle_load_config)
        self.saveButton.clicked.connect(self._handle_save_config)
        menuStack.addWidget(self.loadButton)
        menuStack.addWidget(self.saveButton)
        
        # First Row
        rowStack1= QHBoxLayout()
        self.inputEdit =  QTextEdit("Input here...")
        self.inputEdit.setBaseSize(300, 300)
        self.inputEdit.textChanged.connect( self._handle_text_changed)
        rowStack1.addWidget(self.inputEdit)
        self.tableWidget = QTableWidget()    
        self.tableWidget.setRowCount(CONFIG_ROW)
        self.tableWidget.setColumnCount(2)
        for i in range(CONFIG_ROW):
            self.tableWidget.setItem(i, 0, QTableWidgetItem())
            self.tableWidget.setItem(i, 1, QTableWidgetItem())
        self.tableWidget.setHorizontalHeaderLabels(['Match', 'Action'])
        self.tableWidget.setVerticalHeaderLabels([str(i) for i in range(50)])
        self.tableWidget.setColumnWidth(0, 135)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setFixedWidth(300)
        self.tableWidget.editTriggers
        rowStack1.addWidget(self.tableWidget)

        ### Second Row
        rowStack2= QHBoxLayout()
        self.outputEdit =  QTextEdit("Output here...")
        self.outputEdit.setBaseSize(650, 300)
        rowStack2.addWidget(self.outputEdit)

        window_layout.addLayout(menuStack)
        # window_layout.addStretch(1)
        window_layout.addLayout(rowStack1)
        window_layout.addLayout(rowStack2)
        self.setLayout(window_layout)

        self.setGeometry(300, 300, 280, 170)
        self.resize(700, 650)
        self.setWindowTitle("My Tex Helper")
        self.show()
        
    def _handle_text_changed(self):
        input_str = self.inputEdit.toPlainText()
        criterions = []
        for i in range(CONFIG_ROW):
            match = self.tableWidget.item(i, 0).text()
            action = self.tableWidget.item(i, 1).text()
            if match != "" and action != "":
                criterions.append(parse_criterion_v2(match, action))
        for criteria in criterions:
            input_str = criteria.apply(input_str)
        self.outputEdit.setText(input_str)
        pass


    def _clear_table(self):
        for i in range(CONFIG_ROW):
            self.tableWidget.item(i, 0).setText("")
            self.tableWidget.item(i, 1).setText("")

    def _handle_load_config(self):
        self._clear_table()
        try:
            filename,_ =QFileDialog.getOpenFileName(self, 'Load Configs', os.getcwd(), "ALL Files(*);; Text Files(*.txt)")
            with open(filename, encoding='utf-8') as file_obj:
                lines = file_obj.readlines()
                try:
                    for idx, line in enumerate(lines):
                        line = line
                        criteria = parse_criterion_v1(line)
                        self.tableWidget.item(idx, 0).setText(criteria.match)
                        self.tableWidget.item(idx, 1).setText(criteria.action)
                except Exception as e:
                    print(e)
                    QMessageBox.information(self, "Wrong", "Invalid configure file format.", QMessageBox.No)
        except:
            return
    
    


    def _handle_save_config(self):
        dirname = QFileDialog.getExistingDirectory(self, 'Save Configs', os.getcwd())
        entries = []
        for i in range(CONFIG_ROW):
            match = self.tableWidget.item(i, 0).text()
            action = self.tableWidget.item(i, 1).text()
            if match != "" and action != "":
                entries.append(match + " -> " + action)
        with open(dirname + f"/config_{datetime.now().strftime('%Y_%m_%d_%H_%M')}.txt", mode='a') as f:
            f.write("\n".join(entries))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GitHelperMainW()
    sys.exit(app.exec_())
    input("please input any key to exit!")