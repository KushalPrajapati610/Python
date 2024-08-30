print("Press add for 1")
print("Press sub for 2")
print("Press div for 3")
print("Press mul for 4")
op=int(input("enter option =>"))

if op==1:
    no=int(input("enter no"))
    no1=int(input("enter no"))
    sum=no + no1
    print("sum",sum)
elif op==2:
    no=int(input("enter no"))
    no1=int(input("enter no"))
    sub=no - no1
    print("sub",sub)
elif op==3:
    no=int(input("enter no"))
    no1=int(input("enter no"))
    mul=no * no1
    print("mul",mul)
elif op==4:
    no=int(input("enter no"))
    no1=int(input("enter no"))
    div=no / no1
    print("div", div)
else:
    print("worng")