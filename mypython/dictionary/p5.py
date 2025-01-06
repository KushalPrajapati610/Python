#Sample data:
# marks = {
#     "ram": 33,
#     "rahul": 45,
#     "manav": 30,
#     "jayul": 34,
#     "meena": 29,
#     "siddhi": 48
# }
# Enter key for search: rahul


a = input("Enter key for search =")
marks = {"ram": 33,"rahul": 45,"manav": 30,"jayul": 34,"meena": 29,"siddhi": 48}
if a in marks:
    print("Yes, it exists.")
else:
    print("NO")
