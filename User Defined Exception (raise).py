try:
    a=int(input("Enter a positive integer:\t"))
    if a<=0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
        print(ve)