import math
while True:
    try:
        num=int(input("Enter a number:\t"))
        print("Square root = ",math.sqrt(num))
        break
    except ValueError:
        print("Please Enter a number")
