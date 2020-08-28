import subprocess

# Execute Shell command using Python

print('*********************************')
print(f'Check File System Disk Space Usage')
print('*********************************')
subprocess.call(['df', '-h'])



if __name__ == "__main__":
    pass