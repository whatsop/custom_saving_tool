import os
import sys
import datetime, time
import subprocess

from PySide2 import QtUiTools, QtWidgets

import hou


class SavingReminder(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        UI_FILE = r'D:\PYTHON_ADVANCED_COURSE\tools\saving_reminder_tool\saving_reminder.ui'
        self.ui = QtUiTools.QUiLoader().load(UI_FILE, parentWidget=self)
        
        


win = SavingReminder()
win.show()

