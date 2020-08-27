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
    ''' Move .Doc files from Source to 'DocFiles' folder '''
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


def move_zipfiles(destinationpath):
    ''' Move .zip files from Source to 'zipFiles' folder '''
    dst_fldr = path + 'zipFiles'
    try:
        os.makedirs(path + 'zipFiles')  # it creates the destination folder 'zipFiles'
    except:
        print('Folder already exist or some error')

    files = glob.iglob(os.path.join(path, "*.zip"))
    for zip_files in files:
        if os.path.isfile(zip_files):
            print('zip File is moved', zip_files)
            shutil.move(zip_files, dst_fldr)
            pass


if __name__ == "__main__":
    sourcefolder = 'Source'
    Destinationfolder = 'Destination'
    move_file(path + sourcefolder, path + Destinationfolder)
    move_docfiles(path)
    move_zipfiles(path)
    pass
