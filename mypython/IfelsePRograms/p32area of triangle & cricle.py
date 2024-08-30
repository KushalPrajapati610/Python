print("Enter the op1")
print("Enter the op2")
op=int(input("Enter the option=>"))

if op==1:
    h=int(input("enter h =>"))
    b=int(input("enter b =>"))
    area=h*b*0.5
    print("Area of triangle = ",area)
elif op==2:
    r=int(input("enter r =>"))
    Area=3.14*r*r
    print("Area of circle = ",Area)
else:
    print("wrong number")