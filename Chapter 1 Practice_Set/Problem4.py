import os

# Specify the directory path
path = '/C - Language'

# Get the list of all files and directories
dir_list = os.listdir(path)

# Print the contants of directory

print(f"Contents of '{path}':")
for item in dir_list:
    print(item)
