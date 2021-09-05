#file

import os

source = "C:\\Users\\User\\Desktop\\source.txt"
destination = r"C:\Users\User\Desktop\destination.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")