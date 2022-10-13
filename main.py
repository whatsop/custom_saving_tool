"""
content : a custom saving tool

version : 0.1.0
date : 10/05/2022

how to : start()
dependencies : PySide2, hou

author : Arup Kasimov
"""


import sys

from PySide2 import QtUiTools, QtWidgets, QtCore

import hou
import os
import hou_utils
import os_utils


class CustomSavingTool(QtWidgets.QWidget):

    
    def __init__(self):
        super().__init__()
        
        
        # UI
        UI_FILE = r'D:\PYTHON_ADVANCED_COURSE\tools\saving_reminder_tool\saving_reminder.ui'
        self.ui = QtUiTools.QUiLoader().load(UI_FILE, parentWidget=self)
        
        # set folder path
        self.curr_scene_path = hou.hipFile.path()
        self.curr_scene_name = hou.hipFile.basename()
        self.curr_folder_path = self.curr_scene_path.replace(self.curr_scene_name, "")
        
        # set path line edit
        self.ui.pathLineEdit.setText(self.curr_folder_path)
        
        self.ui.fileNameLineEdit.setText(self.curr_scene_name.split(".")[0])
        
        self.comment = ""

        self.ui.selectFolderPushButton.clicked.connect(self.select_folder)
        self.ui.saveBtn.clicked.connect(self.save_file)

        
    def save_file(self):
        self.comment = self.ui.commentTextEdit.toPlainText()
        new_scene_name = self.ui.fileNameLineEdit.text()
        new_folder_path = self.ui.pathLineEdit.text()
        new_file_name = new_folder_path + "/" + new_scene_name + "." + self.curr_scene_name.split(".")[1]
   
        os_utils.make_txt_file(new_folder_path, new_scene_name, self.comment)
        hou_utils.save_curr_scene(new_file_name)
        
    def select_folder(self):

        folder_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select a directory", self.curr_folder_path)
        self.ui.pathLineEdit.setText(folder_path)

    def closeEvent(self, event):
        # will make sure to kill the application by unparenting the hou qt main window
        self.setParent(None)



#-------------------------------------



def start():
    win = CustomSavingTool()
    win.setParent(hou.qt.mainWindow(), QtCore.Qt.Window) # parenting with hou qt main window so the application does not close directly just after starting
    win.show()
    

start()