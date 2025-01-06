#18. You and your wife argued about expenses last night.
# You both want to know who is spending more in a month.
# Now you both go to the Little Yoda he is a good python programmer.
# He suggested that both of you add an entry in a dictionary next time you spend money.
# So that you can have a clear picture of your expenses and plan to reduce them.
# Both dictionaries are as below-

# Your expenses -
# Clothes - 1100
# Shoes - 1000
# Watch - 900
# Mobile Recharge - 699
# Petrol - 1980

# Your Wife’s expenses -
# Mobile Recharge - 799
# DTH recharge - 999
# Clothes - 2310
# Makeup - 3670
# Shoes - 999

Yourexpenses = {"Clothes": 1100,
                "Shoes": 1000,
                "Watch": 900,
                "Mobile Recharge": 699,
                "Petrol": 1980}

Wifeexpenses = {"Mobile Recharge": 799,
                "DTH recharge": 999,
                "Clothes": 2310,
                "Makeup": 3670,
                "Shoes": 999}

# Find out the total expenses for each of you.

Yourexpenses = sum(Yourexpenses.values())
print("You expense =", Yourexpenses)

Wifeexpenses = sum(Wifeexpenses.values())
print("Wife expenses = ", Wifeexpenses)

# Find out who spending more

if Yourexpenses > Wifeexpenses:
    print("Your")
else:
    print("Wife")

# Find out which thing you and your wife spending more
Yourexpenses = {"Clothes": 1100,
                "Shoes": 1000,
                "Watch": 900,
                "Mobile Recharge": 699,
                "Petrol": 1980}

Wifeexpenses = {"Mobile Recharge": 799,
                "DTH recharge": 999,
                "Clothes": 2310,
                "Makeup": 3670,
                "Shoes": 999}
expenses1 = Yourexpenses.keys()
expenses = Yourexpenses.values()
print(max(expenses1)) ,print((max(expenses)))

expenses = Wifeexpenses.values()
print(max(expenses))