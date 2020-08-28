import glob
import shutil
import os

# OS is Mac
path = '/Users/pboopathi/Downloads/'


def move_file(sourcepath, destinationpath):
    ''' Move files from one folder  to another folder '''

    files = os.listdir(sourcepath)
    print("The files to be moved from source folder to Destination Folder ", files)
    for f in files:
        source = sourcepath + "/" + f
        shutil.move(source, destinationpath)


def move_docfiles(destinationpath):
    ''' Move .Doc files from Source to 'DocFiles' folder '''
    dst_fldr = path + 'DocFiles'
    try:
         if not os.path.exists(path + 'DocFiles'):
            os.makedirs(path + 'DocFiles')  # it creates the destination folder 'DocFiles'
    except:
        print('Some error')

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
        if not os.path.exists(path + 'zipFiles'):
          os.makedirs(path + 'zipFiles')  # it creates the destination folder 'zipFiles'
    except:
        print('Some error')

    files = glob.iglob(os.path.join(path, "*.zip"))
    for zip_files in files:
        if os.path.isfile(zip_files):
            print('zip File is moved', zip_files)
            shutil.move(zip_files, dst_fldr)
            pass


def move_movfiles(destinationpath):
    ''' Move .mov files from Source to 'movFiles' folder '''
    dst_fldr = path + 'movFiles'
    try:
        if not os.path.exists(path + 'movFiles'):
          os.makedirs(path + 'movFiles')  # it creates the destination folder 'zipFiles'
    except:
        print('Some error')

    files = glob.iglob(os.path.join(path, "*.mov"))
    for mov_files in files:
        if os.path.isfile(mov_files):
            print('mov File is moved', mov_files)
            shutil.move(mov_files, dst_fldr)
            pass


if __name__ == "__main__":
    sourcefolder = 'Source'
    Destinationfolder = 'Destination'
    move_file(path + sourcefolder, path + Destinationfolder)
    move_docfiles(path)
    move_zipfiles(path)
    move_movfiles(path)
    pass
