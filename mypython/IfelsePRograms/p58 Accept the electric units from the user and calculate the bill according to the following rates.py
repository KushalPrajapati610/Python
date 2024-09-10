units=int(input("Enter the number of units ="))

if units < 100:
    print("Free")
elif units > 100 and units < 300:
    print("units =", units * 2)
elif units > 300:
    print("units =", (units -300) * 5)
else:
    print("sorry")