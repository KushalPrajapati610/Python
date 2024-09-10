Price = int(input("Enter Market price ="))

if Price > 10000:
    amount = Price * 20/100
    net = Price -Price*20/100
    print("net =",net)
else:
    print("Sorry")