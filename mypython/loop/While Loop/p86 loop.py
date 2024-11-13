while True:
    print("Enter 1 num for addition ")
    print("Enter 2 num for subtraction ")
    print("Enter 3 num for divison ")
    print("Enter 4 num for multiple ")
    print("Enter 5 num for Exit ")
    op = int(input("Enter option ="))

    if op == 1:
        no1 = int(input("Enter the number ="))
        no2 = int(input("Enter the number ="))
        print("Addition",no1 + no2)
    elif op == 2:
        no1 = int(input("Enter the number ="))
        no2 = int(input("Enter the number ="))
        print("Subtraction",no1 - no2)
    elif op == 3:
        no1 = int(input("Enter the number ="))
        no2 = int(input("Enter the number ="))
        print("Divison",no1 / no2)
    elif op == 4:
        no1 = int(input("Enter the number ="))
        no2 = int(input("Enter the number ="))
        print("Mutiple", no1 * no2)
    elif op == 5:
        print("over")
        break
    else :
        print("wrong option")
