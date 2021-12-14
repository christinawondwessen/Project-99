#print ("hello")
import os
import shutil
path=input("enter directory name here")
destination=input("enter destination here")

path=source+"/"
destination=destination+"/"
files=os.listdir(source)
for i in files:
    shutil.copy((source+file),destination)
    name,ext=os.path.splitext(file)