print("Enter 1 for Xerox ")
print("Enter 2 for Type ")
print("Enter 3 for Both 1 & 2 ")
op=int(input("Enter a option ="))

if op==1:
    print("For one xerox= 7rs , More than 50 xerox= 5rs ")
    qty=int(input("Enter no. of xerox ="))
    if qty>50:
        print("Bill of Xerox=", qty * 5)
    else:
        print("Bill of Xerox=" ,qty*7)

elif op==2:
    print("For one type =20rs , More than 50 type =15rs")
    qty=int(input("Enter no. of type ="))
    if qty>50:
        print("Bill of Type=", qty * 15)
    else:
        print("Bill of Type=", qty * 20)
elif op==3:
    print("For one xerox= 7rs , More than 50 xerox= 5rs ")
    b1=b2=0
    qty = int(input("Enter no. of xerox ="))
    if qty > 50:
        b1=qty*5
        print("Bill of Xerox=", b1)
    else:
        b1=qty*7
        print("Bill of Xerox=", b1)

    print("For one type =20rs , More than 50 type =15rs")
    b1=b2=0
    qty = int(input("Enter no. of type ="))
    if qty > 50:
        b2=qty*15
        print("Bill of Type=", qty * 15)
    else:
        b2=qty*20
        print("Bill of Type=", qty * 20)

    print("Bill for both =",  b1 + b2)
else:
    print("Sorry")