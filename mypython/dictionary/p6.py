# 4. Write a Python script to print data in vertical form and display whether that student is pass or fail from the dictionary. (18 marks to pass)
# Sample data:
# marks = {
#     "ram": 33,
#     "rahul": 15,
#     "devesh": 30,
#     "jayul": 34,
#     "jiya": 16,
#     "sadhana": 11,
#     "meena": 19,
#     "karan": 20
# }


marks = {
    "ram": 33,
    "rahul": 15,
    "devesh": 30,
    "jayul": 34,
    "jiya": 16,
    "sadhana": 11,
    "meena": 19,
    "karan": 20}
for key,values in marks.items():
    if values >= 18:
        print(key, values, "pass")
    else:
        print(key, values, "fail")

