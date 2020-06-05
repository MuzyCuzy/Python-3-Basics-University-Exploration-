def readfile(f,name):
    print(f.read())
def writefile(f,name):
    data=input("Enter the data\n")
    f.write(data)
def renamefile(name):
    newname=input("Enter the new file name\n")
    os.rename(name,newname)
def removefile(name):
    os.remove(name)

import os
name=input("Name of the file:\n")
f=open(name,"r+")
choice=int(input("Enter your choice\n1 Read\n2 Write\n3 Rename\n4 Delete/Remove\n"))
if (choice==1):
    readfile(f,name)
elif (choice==2):
    writefile(f,name)
elif (choice==3):
    renamefile(name)
elif (choice==4):
    removefile(name)
else:
    print("Wrong choice\n")
f.close()
