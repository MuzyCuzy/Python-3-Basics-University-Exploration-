while True:
    try:
        name=input("Enter the file name with extension:\t")
        f=open(name,"r")
        print(f.read())
        f.close()
        break
    except IOError:
        print("File not found\n")
