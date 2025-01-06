#7. Write a Python program to remove a key from a dictionary.
# Sample data:
# marks = {"ram": 33,
#          "rahul": 15,
#          "devesh": 30,
#          "jayul": 34,
#          "jiya": 16,
#          "sadhana": 11,
#          "meena": 19}

marks = {"ram": 33,
         "rahul": 15,
         "devesh": 30,
         "jayul": 34,
         "jiya": 16,
         "sadhana": 11,
         "meena": 19}

marks.pop("rahul")
print(marks)
