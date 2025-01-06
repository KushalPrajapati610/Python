try:
    a=int(input("Enter no1 =>"))
    b=int(input("Enter no2 =>"))
    ans=a/b
    print(ans)
except ZeroDivisionError:
    print("Why u enter 0")
except ValueError:
    print("Why u enter string")
except:
    print("Error")