import os
import shutil

def jpg_adder(dir):
    for filename in os.listdir(dir):
        if filename.endswith('jpg'):
            continue
        else:
            filenewname = os.path.join(dir, filename + '.jpg')
            file = os.path.join(dir,filename)
            shutil.move(file, filenewname)

def mp3_finder(dir):
    file_mp3 =[]
    for roots,folders,files in os.walk(dir):
            for file in files:
                file_each = os.path.join(roots,file)
                if file_each.endswith('mp3'):
                    file_mp3.append(file_each)
    return file_mp3
