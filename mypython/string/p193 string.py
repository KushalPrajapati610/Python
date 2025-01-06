# upper->lower

text=input("Enter text =>")
for i in text:
    if i in i.upper():
        print(i.lower(), end="")
    elif i in i.lower():
        print(i.upper(),end="")
