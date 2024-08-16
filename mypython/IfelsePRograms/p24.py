maths=int(input("enter the maths marks="))
english=int(input("enter the english marks="))
SS=int(input("enter the SS marks="))

total=maths+english+SS
print("total =",total)

if total>50:
    print("PASS")
else:
    print("FAIL")