units=int(input("Enter the number of units ="))

if units < 100:
    print("Free")
elif 100 < units < 300:
    print("units =", units * 2)
elif units > 300:
    print("units =", (units -300) * 5)
else:
    print("sorry")
