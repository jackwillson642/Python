import os

print(os.getcwd()) #Prints the Current Working Directory(cwd)
print(os.listdir()) # Prints all the directories in the cwd

os.mkdir('creation') # It creates a directory; if mk is replaced with rm, the directory will be removed
os.makedirs('dir/sub_dir/sub_sub_dir') # It creates intermidiate directories too. If make is replaced with remove, it removes the directory tree.

os.rename('initial.txt','final.txt') #Rename!!

print(os.stat('box.txt'))

