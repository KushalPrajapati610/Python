#9. Write a Python program to count the number of students who passed (marks >= 18) in the dictionary.
# Sample data:
# marks = {"ram": 33,
#     "rahul": 15,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16,
#     "sadhana": 11,
#     "meena": 19,
#     "karan": 20,
#     "anita": 25}

marks = {"ram": 33,
    "rahul": 15,
    "devesh": 30,
    "jayul": 34,
    "jiya": 16,
    "sadhana": 11,
    "meena": 19,
    "karan": 20,
    "anita": 25}
no = int(input("Enter the number ="))
c=0
for no in marks.values():
    if no > 18:
        c=c+1
        print("pass")
    else:
        print("fail")
print("Count of pass =",c)

