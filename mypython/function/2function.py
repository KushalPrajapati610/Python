"""
square()

areaoftri()

areaofcricle()

table()

oddeven()

posneg()

max3()

factorial() 5X4X3X 120

"""


def square():
    a = int(input("Enter the value ="))
    square= a*a
    print("square = ", square)

square()


def areaoftriangle():
    b = int(input("Enter the value of base ="))
    h = int(input("Enter the height ="))
    a = 0.5*(b*h)
    print(" area of triangle =", a)

areaoftriangle()

def areaofcricle():
    r = int(input("Enter the value radius ="))
    a = 3.14*r*r
    print(" area of cricle =",a)

areaofcricle()

def table():
    t = int(input("Enter the number ="))
    for i in (1,11):
        print(t,'x',i,'=',t*i)

table()

def oddeven():
        a = int(input("Enetr the number ="))
        if a % 2==0:
            print("even")
        else:
            print("odd")


def posneg():
    a = int(input("Enter the number ="))
    if a>0:
        print("postive")
    else:
        print("negitive")

oddeven()
posneg()

def max3():
    a = int(input("Enter the number ="))
    b = int(input("Enter the number ="))
    c = int(input("Enter the number ="))
    if a>b and a>c:
        print("no1 is greater")
    elif b>a and b>c:
        print("no2 is greater")
    else:
        print("no3 is greater")


def factorial():
    num = int(input("Enter the number ="))
    factorial = 1
    for i in range(1,num+1):
        print(i,end="x")
        factorial = factorial*i
        print("factorial =", factorial)


max3()
factorial()

