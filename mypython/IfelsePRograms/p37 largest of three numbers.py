no1=int(input("enter no1 ="))
no2=int(input("enter no2 ="))
no3=int(input("enter no3 ="))

if no1>no2 and no1>no3:
    print("Greater no is 1")
elif no2>no1 and no2>no3:
    print("Greater no is 2")
elif no3>no1 and no3>no2:
    print("Greater no is 3")
else:
    print("Sorry")