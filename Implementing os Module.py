import os
os.mkdir("myfolder")#creates a new file/dir called myfolder in the current Python path
a=os.listdir(os.curdir)#lists all the files and folders in current dir
print(a)
os.rmdir("myfolder")#deletes dir myfolder from current Python path
