#8. Write a Python program to find the maximum and minimum marks from a dictionary.
# Sample data:
# marks = {"ram": 33,
#     "rahul": 45,
#     "devesh": 30,
#     "jayul": 34,
#     "meena": 29,
#     "karan": 40,
#     "anita": 18,
#     "siddhi": 25}

marks = {"ram": 33,
    "rahul": 45,
    "devesh": 30,
    "jayul": 34,
    "meena": 29,
    "karan": 40,
    "anita": 18,
    "siddhi": 25}
max = max(marks.values())
print("Max= ",max)
min = min(marks.values())
print("Min=",min)
