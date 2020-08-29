import subprocess

# Execute Shell command using Python
from glob import glob

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


if __name__ == "__main__":
    popen_redirectoutputtofile()
    listing_files_in_currentDirectory()
    pass
