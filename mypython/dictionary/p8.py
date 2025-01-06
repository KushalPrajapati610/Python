#6. Write a Python program to sum all the items in a dictionary.
# Sample data:
# items = {
#     "maggie": 20,
#     "parleg": 10,
#     "crackjack": 20,
#     "noodles": 32,
#     "chips": 15,
#     "cookies": 18
# }


items = {"maggie": 20,
         "parleg": 10,
         "crackjack": 20,
         "noodles": 32,
         "chips": 15,
         "cookies": 18}
total = sum(items.values())
print(total)
