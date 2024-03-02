import os

filename = input("Path: ")

if os.path.exists(filename):
    print(os.path.basename(filename))
    print(os.path.basename(os.path.dirname(filename)))