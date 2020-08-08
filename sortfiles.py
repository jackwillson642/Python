import os
import shutil

dir = os.environ['HOME']+'/'+'downloads/'
os.chdir(dir)

files = os.listdir(dir)
for file in files:
    if os.path.isfile(file):
        split_file = os.path.splitext(file)
        ext = ((split_file[-1]).replace('.',''))+'/'
        if not os.path.isdir(ext):
            os.mkdir(ext)
        shutil.move(file,ext+file)
