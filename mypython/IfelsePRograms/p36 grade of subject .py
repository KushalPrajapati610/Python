maths=int(input("enter the maths marks ="))
SS=int(input("enter the SS marks ="))
english=int(input("enter the english ="))
total = maths + SS + english
print("total =",total)

if total>0 and total<50:
    print("C Grade")

elif total>50 and total<100:
    print("B Grade")

elif total>100:
    print("A Grade")

else:
    print("sorry")