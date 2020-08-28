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

    pass


if __name__ == "__main__":
    popen_redirectoutputtofile()
    pass
