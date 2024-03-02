import os

f = input()

if os.path.exists(f):
    print("File exists!")
else:
    print("Does not exist!")

if os.access(f, os.R_OK):
    print("We can read")
else:
    print("Can't read")
if os.access(f, os.W_OK):
    print("We can write")
else:
    print("Can't write")
if os.access(f, os.X_OK):
    print("We can execute")
else:
    print("Can't exeucte")