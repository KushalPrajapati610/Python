t1=0
t2=0
t3=0
t4=0
t5=0
while True:
    print("Enter 1 for Burger")
    print("Enter 2 for Pizza")
    print("Enter 3 for Sandwich")
    print("Enter 4 for Pasta")
    print("Enter 5 for Milkshake")
    print("Enter 6 for Exit")
    op = int(input("Enter the number for food ="))

    if op == 1:
        print("Burger price 100")
        no = int(input("How many you want="))
        t1=no * 100
        print("Bill=", no * 100)
    elif op == 2:
        print("Pizza price 200")
        no = int(input("How many you want="))
        t2=no*200
        print("Bill=", no * 200)
    elif op == 3:
        print("Sandwich price 150")
        no = int(input("How many you want="))
        t3=no*150
        print("Bill=", no * 150)
    elif op == 4:
        print("Pasta price 170")
        no = int(input("How many you want="))
        t4=no*170
        print("Bill=", no * 170)
    elif op == 5:
        print("Milkshake price 120")
        no = int(input("How many you want="))
        t5=no*120
        print("Bill", no * 120)
    elif op == 6:
        Total = t1 + t2 + t3 + t4 + t5
        print("Total Bill =", Total)
        print("Over")
        break
    else:
        print("wrong option")


