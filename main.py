"""
content : a custom saving tool

version : 0.1.0
date : 10/05/2022

how to : start()
dependencies : PySide2, hou

author : Arup Kasimov
"""

import os
import sys



from PySide2 import QtUiTools, QtWidgets, QtCore

import hou


class CustomSavingTool(QtWidgets.QWidget):

    
    def __init__(self):
        super().__init__()
        
        
        # UI
        UI_FILE = r'D:\PYTHON_ADVANCED_COURSE\tools\saving_reminder_tool\saving_reminder.ui'
        self.ui = QtUiTools.QUiLoader().load(UI_FILE, parentWidget=self)
        
        # path line edit
        CURR_SCENE_PATH = hou.hipFile.path()
        self.curr_scene_name = hou.hipFile.basename()
        self.curr_folder_path = CURR_SCENE_PATH.replace(self.curr_scene_name, "")
        
        self.ui.pathLineEdit.setText(self.curr_folder_path)
        
        self.comment = ""

        self.ui.saveBtn.clicked.connect(self.save_file)

        
    def save_file(self):
        self.comment = self.ui.commentTextEdit.toPlainText()


    def closeEvent(self, event):
        # will make sure to kill the application by unparenting the hou qt main window
        self.setParent(None)



#-------------------------------------



def start():
    win = CustomSavingTool()
    win.setParent(hou.qt.mainWindow(), QtCore.Qt.Window) # parenting with hou qt main window so the application does not close directly just after starting
    win.show()
    

start()