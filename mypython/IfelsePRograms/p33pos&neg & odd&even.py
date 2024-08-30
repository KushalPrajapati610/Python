print ("enter op1 ")
print ("enter op2 ")
op=int(input("enter the option "))

if op==1:
    no=int(input("enter the value of=>"))
    if no>0:
      print("no is positive")
    else:
      print("no is negative")
elif op==2:
     no=int(input("enter the value of=>"))
     if no % 2==0:
        print("no is even")
     else:
        print("no is odd")
else:
   print("Wrong opt")

