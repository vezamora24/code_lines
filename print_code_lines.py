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

files = os.listdir(folder)[1:]
print (files)

files_dict = {files[i]: 0 for i in range(len(files))}
print (files_dict)

extensions = [f.split(".")[1] for f in files if "." in f]
#print (extensions)

e_set = list(set(extensions))
#print (e_set)

e_dict = {e_set[i]: 0 for i in range(len(e_set))}
print (e_dict)