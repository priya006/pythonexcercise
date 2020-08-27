import shutil
import os


def move_file(sourcepath, destinationpath):
    files = os.listdir(sourcepath)
    print("The files to be moved ", files)
    print("Source path", sourcepath)
    print("Destination Path", destinationpath)
    for f in files:
        source = sourcepath + "/" + f
        shutil.move(source, destinationpath)


if __name__ == "__main__":
    sourcepath = '/Users/pboopathi/Downloads/Source'
    destinationpath = '/Users/pboopathi/Downloads/Destination'
    move_file(sourcepath, destinationpath)
    pass
