import shutil
import os

sourcepath = '/Users/pboopathi/Downloads/Source'
destinationpath = '/Users/pboopathi/Downloads/Destination'

files = os.listdir(sourcepath)
print("The files to be moved ",files)
print("Source path", sourcepath)
print("Destination Path", destinationpath)
for f in files:
    source = sourcepath+"/"+f
    shutil.move(source, destinationpath)

