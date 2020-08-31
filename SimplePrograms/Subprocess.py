import fnmatch
import os
import subprocess

# Execute Shell command using Python


print('*********************************')
print(f'Check File System Disk Space Usage')
print('*********************************')
subprocess.call(['df', '-h'])

print('********************************************************')
print(f'Check Information of all File System Disk Space Usage')
print('********************************************************')
subprocess.call(['df', '-a'])

print('************')
print(f'List Files')
print('************')
subprocess.call(['ls', '-lah'])


def popen_redirectoutputtofile():
    path_to_output_file = "/Users/pboopathi/Desktop/python"
    output = open(path_to_output_file, 'w+')
    print('**************************************************')
    print('Writting to file in the path --> ', path_to_output_file)
    process = subprocess.Popen(["ls", "-a"], stdout=output, stderr=subprocess.PIPE, universal_newlines=True)
    output, errors = process.communicate()

    # stdout has been written to this file.The File content is read and displayed to standard  output
    with open(path_to_output_file, "r") as f:
        print(f.read())
    pass


def listing_files_in_currentDirectory():
    # ls -p . | grep -v /$
    ls = subprocess.Popen(["ls", "-p", "."], stdout=subprocess.PIPE)
    grep = subprocess.Popen(["grep", "-v", "/$"], stdin=ls.stdout, stdout=subprocess.PIPE)
    endOfPipe = grep.stdout

    for line in endOfPipe:
        print('Listing files', line)

    pass


def list_pythonfiles():
    listOffiles = os.listdir('.')
    print('listoffilesinthecurrentdirectory -->', listOffiles)
    pattern = '*.py'
    for file in listOffiles:
        if fnmatch.fnmatch(file, pattern):
            # Test whether FILENAME matches PATTERN
            print("pythonfilename:", file)

    pass


def find_files():
    # Set up find command
    findCMD = 'find . -name "*.py"'

    out = subprocess.Popen(findCMD, shell=True, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Get standard out and error
    (stdout, stderr) = out.communicate()

    # Save found files to list
    filelist = stdout.decode().split()
    print('*********************************')
    print(f'Current path')
    print('*********************************')
    subprocess.call('pwd')
    print('Findthe files',filelist)
    pass


if __name__ == "__main__":
    popen_redirectoutputtofile()
    listing_files_in_currentDirectory()
    list_pythonfiles()
    find_files()
    pass
