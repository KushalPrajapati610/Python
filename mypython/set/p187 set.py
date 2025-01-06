#18. Write a Python program to check if one set is a superset of another.

# Hint: Use the issuperset() method to check if all elements of another set are contained in the current set.

# Sample data:
# s1 = {11, 22, 33, 44, 55}
# s2 = {11, 22}
# Expected Output: True

s1 = {11, 22, 33, 44, 55}
s2 = {11, 22}
print(s1.issuperset(s2))
