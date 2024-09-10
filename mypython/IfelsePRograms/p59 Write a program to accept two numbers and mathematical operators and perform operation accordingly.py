no1 = int(input("enter first no ="))
no2 = int(input("enter second no ="))
op = input("enter operator =")

if op == '+':
    sum = no1 + no2
    print("sum=", sum)
elif op == '-':
    sub = no1 + no2
    print("sub=", sub)
elif op == '*':
    mul = no1 * no2
    print("mul=", mul)
elif op == '/':
    div = no1 / no2
    print("div=", div)
else:
    print("sorry")
