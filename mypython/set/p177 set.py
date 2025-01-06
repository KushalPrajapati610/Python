#8. Write a Python program to check if a set is a subset of another set.

# Hint: Use the issubset() method to check if all elements of one set are present in another.

# Sample data:
# s1 = {11, 22, 33, 44, 55}
# s2 = {11, 22, 55}
# Expected Output: True


s1 = {11, 22, 33, 44, 55}
s2 = {11, 22, 55}
print(s1.issuperset(s2))
