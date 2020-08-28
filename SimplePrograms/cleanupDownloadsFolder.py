import glob
import shutil
import os

# OS is Mac
path = '/Users/pboopathi/Downloads'


def move_file(sourcepath, destinationpath):
    ''' Move files from one folder  to another folder '''

    files = os.listdir(sourcepath)
    print("The files to be moved from source folder to Destination Folder ", files)
    for f in files:
        source = sourcepath + "/" + f
        shutil.move(source, destinationpath)


def move_docfiles(destinationpath):
    ''' Move .Doc files from Source to 'DocFiles' folder '''
    dst_fldr = path + '/DocFiles'
    try:
        if not os.path.exists(path + 'DocFiles'):
            os.makedirs('DocFiles')  # it creates the destination folder 'DocFiles'
    except:
        print('Some error')

    files = glob.iglob(os.path.join(path, "*.doc"))
    for doc_files in files:
        if os.path.isfile(doc_files):
            print('Doc File is moved', doc_files)
            # shutil.move(doc_files, dst_fldr)
            try:
                if not os.path.isfile(dst_fldr):
                    shutil.move(os.path.join(doc_files), os.path.join(dst_fldr))
            except:
                print('File already is avilable')
    pass


def move_zipfiles(destinationpath):
    ''' Move .zip files from Source to 'zipFiles' folder '''
    dst_fldr = path + '/zipFiles'
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
    dst_fldr = path + '/movFiles'
    try:
        if not os.path.exists(path + 'movFiles'):
            os.makedirs(path + 'movFiles')  # it creates the destination folder 'movFiles'
    except:
        print('Some error')

    files = glob.iglob(os.path.join(path, "*.mov"))
    for mov_files in files:
        if os.path.isfile(mov_files):
            print('mov File is moved', mov_files)
            # shutil.move(mov_files, dst_fldr)
            # shutil.move(os.path.join(path, mov_files), os.path.join(dst_fldr, mov_files))
            try:
                if not os.path.isfile(dst_fldr):
                    shutil.move(os.path.join(mov_files), os.path.join(dst_fldr))
            except:
                print('File already is avilable')
            print(path)
            pass


def move_pdffiles(destinationpath):
    ''' Move .pdf files from Source to 'pdfFiles' folder '''
    dst_fldr = path + '/pdfFiles'
    try:
        if not os.path.exists(path + 'pdfFiles'):
            os.makedirs(path + 'pdfFiles')  # it creates the destination folder 'pdfFiles'
    except:
        print('Some error')

    files = glob.iglob(os.path.join(path, "*.pdf"))
    for mov_files in files:
        if os.path.isfile(mov_files):
            print('pdf File is moved', mov_files)
            shutil.move(mov_files, dst_fldr)
            pass


def move_csvfiles(destinationpath):
    ''' Move .csv files from Source to 'csvFiles' folder '''
    dst_fldr = path + '/csvFiles'
    try:
        if not os.path.exists(path + 'csvFiles'):
            os.makedirs(path + 'csvFiles')  # it creates the destination folder 'csvFiles'
    except:
        print('Some error')

    files = glob.iglob(os.path.join(path, "*.csv"))
    for mov_files in files:
        if os.path.isfile(mov_files):
            print('csv File is moved', mov_files)
            shutil.move(mov_files, dst_fldr)
            pass


def move_pngfiles(destinationpath):
    ''' Move .png files from Source to 'pngFiles' folder '''
    dst_fldr = path + '/pngFiles'
    try:
        if not os.path.exists(path + 'pngFiles'):
            os.makedirs(path + 'pngFiles')  # it creates the destination folder 'pngFiles'
    except:
        print('Some error')

    files = glob.iglob(os.path.join(path, "*.png"))
    for mov_files in files:
        if os.path.isfile(mov_files):
            print('png File is moved', mov_files)
            shutil.move(mov_files, dst_fldr)
            pass


def move_dmgfiles(destinationpath):
    ''' Move .dmg files from Source to 'dmgFiles' folder '''
    dst_fldr = path + '/dmgFiles'
    try:
        if not os.path.exists(path + 'dmgFiles'):
            os.makedirs(path + 'dmgFiles')  # it creates the destination folder 'dmgFiles'
    except:
        print('Some error')

    files = glob.iglob(os.path.join(path, "*.dmg"))
    for mov_files in files:
        if os.path.isfile(mov_files):
            print('dmg File is moved', mov_files)
            shutil.move(mov_files, dst_fldr)
            pass


def move_xlsxfiles(destinationpath):
    ''' Move .xlsx files from Source to 'xlsxFiles' folder '''
    dst_fldr = path + '/xlsxFiles'
    try:
        if not os.path.exists(path + 'xlsxFiles'):
            os.makedirs(path + 'xlsxFiles')  # it creates the destination folder 'xlsxFiles'
    except:
        print('Some error')

    files = glob.iglob(os.path.join(path, "*.xlsx"))
    for mov_files in files:
        if os.path.isfile(mov_files):
            print('xlsx File is moved', mov_files)
            shutil.move(mov_files, dst_fldr)
            pass


def move_docxfiles(destinationpath):
    ''' Move .docx files from Source to 'docxFiles' folder '''
    dst_fldr = path + '/docxFiles'
    try:
        if not os.path.exists(path + 'docxFiles'):
            os.makedirs(path + 'docxFiles')  # it creates the destination folder 'docxFiles'
    except:
        print('Some error')

    files = glob.iglob(os.path.join(path, "*.docx"))
    for mov_files in files:
        if os.path.isfile(mov_files):
            print('docx File is moved', mov_files)
            shutil.move(mov_files, dst_fldr)
            pass


def move_mp4files(destinationpath):
    ''' Move .mp4 files from Source to 'mp4Files' folder '''
    dst_fldr = path + '/mp4Files'
    try:
        if not os.path.exists(path + 'mp4Files'):
            os.makedirs(path + 'mp4Files')  # it creates the destination folder 'mp4Files'
    except:
        print('Some error')

    files = glob.iglob(os.path.join(path, "*.mp4"))
    for mov_files in files:
        if os.path.isfile(mov_files):
            print('mp4 File is moved', mov_files)
            # shutil.move(mov_files, dst_fldr)
            try:
                if not os.path.isfile(dst_fldr):
                    shutil.move(os.path.join(mov_files), os.path.join(dst_fldr))
            except:
                print('File already is avilable')
            pass


def move_jsonfiles(destinationpath):
    ''' Move .json files from Source to 'jsonFiles' folder '''
    # create the folder manually
    dst_fldr = path + '/FormattedJson'
    try:
        if not os.path.exists(path + 'FormattedJson'):
            os.makedirs(path + 'FormattedJson')  # it creates the destination folder 'JsonFiles'
    except:
        print('Some error')

    files = glob.iglob(os.path.join(path, "*.json"))
    for json_files in files:
        if os.path.isfile(json_files):
            print('json File is moved', json_files)
            # shutil.move(mov_files, dst_fldr)
            try:
                if not os.path.isfile(dst_fldr):
                    shutil.move(os.path.join(json_files), os.path.join(dst_fldr))
            except:
                print('File already is avilable')
            pass


if __name__ == "__main__":
    sourcefolder = '/Source'
    Destinationfolder = '/Destination'
    move_file(path + sourcefolder, path + Destinationfolder)
    move_docfiles(path)
    move_zipfiles(path)
    move_movfiles(path)
    move_pdffiles(path)
    move_csvfiles(path)
    move_pngfiles(path)
    move_xlsxfiles(path)
    move_docxfiles(path)
    move_mp4files(path)
    move_jsonfiles(path)
    pass
