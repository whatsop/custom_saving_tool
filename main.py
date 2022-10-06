import os
import sys
import datetime, time
import subprocess

from PySide2 import QtUiTools, QtWidgets, QtCore

import hou


class SavingReminder(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        UI_FILE = r'D:\PYTHON_ADVANCED_COURSE\tools\saving_reminder_tool\saving_reminder.ui'
        self.ui = QtUiTools.QUiLoader().load(UI_FILE, parentWidget=self)
        


        
        self.ui.saveBtn.clicked.connect(self.save_file)



    def closeEvent(self, event):
        self.setParent(None)
        
    def save_file(self):
        self.comment = self.ui.commentTextEdit.toPlainText()






def start():
    win = SavingReminder()
    win.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
    win.show()

start()