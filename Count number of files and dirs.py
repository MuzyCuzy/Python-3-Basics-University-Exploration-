import os
a=os.listdir(os.curdir)
f=0;d=0
for i in a:
    if (os.path.isfile(i)):
        f+=1
    else:
        d+=1
print("No. of files = ",f,"\nNo. of folders = ",d)
    
