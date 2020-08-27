import glob
import shutil
import os

#OS is Mac
path = '/Users/pboopathi/Downloads/'

def move_file(sourcepath, destinationpath):
    ''' Move files from one folder  to another folder '''

    files = os.listdir(sourcepath)
    print("The files to be moved ", files)
    print("Source path", sourcepath)
    print("Destination Path", destinationpath)
    for f in files:
        source = sourcepath + "/" + f
        shutil.move(source, destinationpath)


def move_docfiles(destinationpath):
    dst_fldr = path + 'DocFiles'
    try:
        os.makedirs(path + 'DocFiles')  # it creates the destination folder 'DocFiles'
    except:
        print('Folder already exist or some error')

    files = glob.iglob(os.path.join(path, "*.doc"))
    for doc_files in files:
        if os.path.isfile(doc_files):
            print('Doc File is moved', doc_files)
            shutil.move(doc_files, dst_fldr)
            pass


if __name__ == "__main__":
    sourcefolder = 'Source'
    Destinationfolder = 'Destination'
    move_file(path + sourcefolder, path + Destinationfolder)
    move_docfiles(path)
    pass
