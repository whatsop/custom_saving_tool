"""
content : a tool that will pop up every x minutes to ask if you would like to save your current scene, you can add a comment
which will create a txt file with the comment you have written inside

version : 0.1.0
date : 10/05/2022

how to : 
dependencies : PySide2, hou

author : Arup Kasimov
"""

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
        

        self.comment = None

        self.ui.saveBtn.clicked.connect(self.save_file)




        
    def save_file(self):
        self.comment = self.ui.commentTextEdit.toPlainText()

    def closeEvent(self, event):
        # will make sure to kill the application by unparenting the hou qt main window
        self.setParent(None)






def start():
    win = SavingReminder()
    win.setParent(hou.qt.mainWindow(), QtCore.Qt.Window) # parenting with hou qt main window so the application does not close directly just after starting
    win.show()

start()