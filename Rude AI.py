print("Type any one of the following dialogues into your console:\nHey\nHowdy\nHi\nHello")
userwords=["Hey","Howdy","Hi","Hello"]
user=input("\nEnter:\n")
response=["Do Not Disturb","Bleh Bleh Bleh [Like the one from Hotel Transylvania]",":X"]
if user.title() in userwords:
    import random
    a=random.randint(0,2)
    print(response[a])
    
