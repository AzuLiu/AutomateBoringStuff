# Copy the files you want.
# 1.Define the folder and file extension;
# 2 .Search the files in this folder and copy these to a new folder.

import os,shutil

def selectiveCopy(path,folder):
    # 2.Search and copy.
    for roots,dirs,files in os.walk(path):
        for f in files:
            print(os.path.abspath(f))
            if f.endswih(fileEx):
                shutil.copy(os.path.join(roots, f),folder)

# 1.Path and file extension.
path = input('Path: ')
folder = input('Folder:')
fileEx = input('File extension:')
#selectiveCopy(path,folder)

