def menu():
    while True:
        try:
            choice=int(input("\n1 New Account\n2 Delete Account\n3 Search Account\n4 Display all Accounts\n5 Exit\nEnter your choice:\t"))
            break
        except ValueError:
            print("Enter the correct number\n")
    if (choice==1):
        newacc()
        menu()
    elif (choice==2):
        deleteacc()
        menu()
    elif (choice==3):
        searchacc()
        menu()
    elif (choice==4):
        displayall()
        menu()
    elif (choice==5):
        exitpro()
    else:
        print("Wrong choice entered\n")
        menu()

def newacc():
    while True:
        try:
            num=int(input("Enter the account number:\t"))
            if (os.path.isfile(str(num)+".txt")):
                raise IOError
            break
        except ValueError:
            print("Account number should be integer number")
        except IOError:
            print("Account number already exists , please choose some other number")
    num1=str(num)+".txt"
    name=input("Enter the account name:\t")
    while True:
        try:
            initialbal=int(input("Enter the initial balance.(Minimum requirement is 1000)\n"))
            if (initialbal<1000):
                raise IOError
            else:
                break
        except ValueError:
            print("Balance should be number")
        except IOError:
            print("Minimum requirment is 1000")
    data=["\tAccountName\tBalance\n\t",name,"\t\t",str(initialbal)]
    with open(num1,"w") as f:
        for i in data:
            f.write(i)
        print("Account number ",num,"Successfully created")

def deleteacc():
        while True:
            try:
                num=int(input("Enter the account number you want to remove:\t"))
                break
            except ValueError:
                print("Account number should be integer number\n")
        num1=str(num)+".txt"
        try:
            os.remove(num1)
            print("Account number ",num,"Successfully deleted")
        except FileNotFoundError:
            print("This account number doesn't exist")

def searchacc():
    while True:
        try:
            num=int(input("Enter the account number you want to search:\t"))
            break
        except ValueError:
            print("Account number should be integer number\n")
    num=str(num)+".txt"
    try:
        if (os.path.isfile(num)):
            b=input("Account exists.Do you want to display its contents?Press y/Y for yes.\t")
            if (b=="y" or b=="Y"):
                with open(num,"r")as f:
                    print(f.read())
            dw=input("Do you want to deposit or withdraw any amount?Press y/Y to do so\t")
            if (dw=="y" or dw=="Y"):
                c=int(input("Enter your choice\n1 Deposit\n2 Withdraw\t"))
                if (c==1):
                    amount=int(input("Enter the amount to deposit\t"))
                    with open (num,"r+")as f:
                        r=f.read()
                        s=r.split("\t")
                        s[0]="\t"
                        s.insert(2,"\t")
                        s.insert(4,"\t")
                        s[6]="\t\t"
                        s[7]=int(s[7])+amount
                        f.seek(0)
                        for i in s:
                                f.write(str(i))
                        f.seek(0)
                        print(f.read())
                elif (c==2):
                    amount=int(input("Enter the amount to withdraw\t"))
                    with open (num,"r")as f:
                        r=f.read()
                        s=r.split("\t")
                        if (int(s[5])>amount):
                            s[0]="\t"
                            s.insert(2,"\t")
                            s.insert(4,"\t")
                            s[6]="\t\t"
                            s[7]=int(s[7])-(amount)
                            f.seek(0)
                            with open (num,"w")as fw:
                                for i in s:
                                    fw.write(str(i))
                            f.seek(0)
                            print(f.read())
                        else:
                            print("Withdrawl amount greater than deposited amount\n")
                else:
                    print("Wrong choice entered\n")
        else :
            raise FileNotFoundError
    except FileNotFoundError:
        print("File with this account number doesn't exist")
    except ValueError:
        print("Choice should be the number provided")

def displayall():
    count=0
    a=os.listdir(os.curdir)
    for i in a:
        if (os.path.isfile(i)):
            count+=1
            print(i)
    print("Total number of accounts = ",count)

def exitpro():
    print("GoodBye!")
    
import os

try:
    os.chdir("Python Bank App Files")
except FileNotFoundError:
    os.mkdir("Python Bank App Files")
os.chdir("Python Bank App Files")
menu()
