<h1> custom saving tool </h1>

### **Introduction**

A tool for saving your current houdini scene and add a comment, which will create a .txt file int the same folder. 
The idea behind is to keep track of what you did on a spefific saved scene, think about it like a "commit"


### **How to use it ?**

There are several ways of using it inside Houdini, but this is one will work :
First, in houdini, you need to create a new shelf, if you do not have any custom shelf already, then create a new tool, you edit the tool and copy paste this :

```
import sys
sys.path.append("D:\\PYTHON_ADVANCED_COURSE\\tools\\saving_reminder_tool\\")

import main
import os_utils
import hou_utils
from importlib import reload
reload(main)
reload(os_utils)
reload(hou_utils)

def CreateInterface():
    return main.start()
```
