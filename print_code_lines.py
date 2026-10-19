import os, sys

current = os.getcwd()
print (f"we are in {current} folder")

folder = input ("Enter folder to scan: ")

if not os.path.exists(folder):
    print (f"Folder {folder} does not exist")
    sys.exit(0)
else:
    print ("Folder exists, continue scanning")
print ("Continue")
