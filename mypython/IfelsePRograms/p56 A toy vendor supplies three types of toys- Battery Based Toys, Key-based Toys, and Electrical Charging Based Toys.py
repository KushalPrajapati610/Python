#The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.
#On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a discount of 10% is given
# on orders for electrical charging based toys of value more than Rs. 500.

print("enter 1 for battery based toys =")
print("enter 2 for key based toys =")
print("enter 3 for electrical toys =")
op=int(input("enter the option ="))

if op==1:
    price = int(input("enter the price ="))
        if price<1000:
            print("price*0.10")
        else:
            print("sorry no discount")

elif op==2:
    price = int(input("enter the price ="))
        if price<100:
            print("price*0.05")
        else:
            print("sorry no discount")

elif op==3:
    price = int(input("enter the price ="))
        if price<500:
            print("price*0.10")
        else:
            print("sorry no discount")

else:
    print("sorry")
