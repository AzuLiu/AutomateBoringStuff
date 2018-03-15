import os, send2trash

def delunneed(path):
    for roots, dirs, files in os.walk(path):
        for f in files:
            if os.path.getsize(os.path.join(roots, f)) > 5*10**6:
                print('Send %s to trash bin.' % (os.path.join(roots, f)))
                send2trash.send2trash(os.path.join(roots, f))

path = input('Path:')
delunneed(path)
