print("Enter 1 for Pizza")
print ("Enter 2 for Buger")
print ("Enter 3 for Cheese Panner")
print ("Enter 4 for Dosa")
print ("Enter 5 for Naan")
op=int(input("enter the option ="))

if op==1:
    print("PIZZA Price is 300")
    qty=int(input("Enter qty =>"))
    print("Bill of Pizza = " ,qty*300)
elif op==2:
    print("Buger Price is 200")
    qty=int(input("Enter qty ="))
    print("Bill of Buger =" ,qty*200)
elif op==3:
    print("Cheese Panner Price is 500")
    qty=int(input("Enter qty ="))
    print("Bill of Cheese Panner" ,qty*500)
elif op==4:
    print("Dosa Price is 150")
    qty=int(input("Enter qty="))
    print("Bill of Dosa" ,qty*150)
elif op==5:
    print("Naan Price is 50")
    qty=int(input("Enter qty"))
    print("Bill of Naan" ,qty*50)
else:
    print("Sorry")