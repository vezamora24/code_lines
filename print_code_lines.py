import os, sys

current = os.getcwd()
print (f"we are in {current} folder")

folder = input ("Enter folder to scan: ")

if not os.path.exists(folder):
    print (f"Folder {folder} does not exist")
    sys.exit(0)
else:
    print ("Folder exists, continue scanning")

#folder = "code"

files = os.listdir(folder)[1:]
#print (files)

files_dict = {files[i]: 0 for i in range(len(files))}
#print (files_dict)

extensions = [f.split(".")[1] for f in files]
#print (extensions)

e_set = list(set(extensions))
print ("set " , e_set)

e_dict = {e_set[i]: 0 for i in range(len(e_set))}
#print (e_dict)

for k in files_dict:
    with open (folder + os.sep + k, "r") as r:
        read = r.readlines()
    files_dict[k] = len(read)

#print (files_dict)
for k in files_dict:
    ext_key = k.split(".")[1]
    e_dict[ext_key] += files_dict[k]

#print (e_dict)
total = sum(e_dict.values())

for k in e_dict:
    value = e_dict[k]/total * 100
    r_value = round(value, 2)
    e_dict[k] = str(r_value) + "%"

for k in e_dict:
    print (k, ":", e_dict[k])