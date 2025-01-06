# upper? lower?

text = input("Enter Text =")
c1 = 0
c2 = 0
for i in text:
    if i in i.lower():
        print(i.upper(),end="")
        c1 = c1+1
    elif i in i.upper():
        print(i.lower(),end="")
        c2 = c2+1
print("\nLowercase Count =",c1)
print("UppercaseCount=",c2)
