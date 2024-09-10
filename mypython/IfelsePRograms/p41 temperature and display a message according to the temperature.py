temp=int(input("enter the temperature no="))

if temp<0:
    print("freezing Atmosphere")
elif temp>0 and temp<10:
    print("very cold atmosphere")
elif temp>10 and temp<20:
    print("Cold Atmosphere ")
elif temp>20 and temp<30:
    print("normal Atmosphere")
elif temp>30 and temp<40:
    print("hot atmosphere")
elif temp>40:
    print("very hot atmosphere")
else:
    print("Sorry")