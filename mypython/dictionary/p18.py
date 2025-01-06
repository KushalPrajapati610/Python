#16. You are given following list of stocks and their prices in last 3 days,

# Stock 	Prices
# info 	[600,630,620]
# ril 	[1430,1490,1567]
# mtl 	[234,180,160]

# Write a program that asks user for operation. Value of operations could be,

# option 1, print: When user enters print it should print following,

# info ==> [600, 630, 620] ==> avg:  616.67
# ril ==> [1430, 1490, 1567] ==> avg:  1495.67
# mtl ==> [234, 180, 160] ==> avg:  191.33

# option 2, add: When user enters 'add', it asks for stock ticker and price.
# If stock already exist in your list (like info, ril etc) then it will append the price to the list.
# Otherwise it will create new entry in your dictionary. For example entering 'tata' and
# 560 will add tata ==> [560] to the dictionary of stocks.

stock = {"info":[600,630,620],
 "ril":[1430,1490,1567],
 "mtl":[234,180,160]}
print("Press 1 for average")
print("Press 2 for add")
op = int(input("Enter for options ="))
if op == 1:
 for key,value in stock.items():
  avg= sum(value)/3
  print(key ,"=", value,"=", avg)

elif op == 2:
 stk = input("Enter Stock name =")
 if stk in stock:
  print("That is Exist")
 else:
  price = int(input("Enter Price="))
  stock[stk] = price
  print(stock)
