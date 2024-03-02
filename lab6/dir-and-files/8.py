import os

filename = input("Path: ")

if os.path.exists(filename):
    if os.access(filename, os.R_OK):
        if os.access(filename, os.W_OK):
            if os.access(filename, os.X_OK):
                os.remove(filename)
            else:
                print("Can't exacute")
        else:
            print("Can't write")
    else:
        print("Can't read")
else:
    print("File doesn't exist")