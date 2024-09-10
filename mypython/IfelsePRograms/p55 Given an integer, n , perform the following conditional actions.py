integer = int(input("Enter a number= "))

if integer % 2 != 0:
    print("Werid")
elif integer % 2 == 0:
    print(integer)
    if integer > 2 and integer < 5:
        print("Not Werid")
    elif integer > 6 and integer < 20:
        print("Werid")
    elif integer < 20:
        print("Not Werid")
    else:
        print(".")
else:
    print("Sorry")
