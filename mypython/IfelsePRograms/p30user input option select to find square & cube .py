print("Enter the op1")
print("Enter the op2")
op=int(input("Enter option =>"))

if op==1:
    no=int(input("enter no"))
    suq=no * no
    print("Square ", suq)
elif op==2:
    no = int(input("enter no"))
    cube=no * no * no
    print("cube",cube)
else:
    print("wrong")