#14. Write a Python program to check if two sets have any common elements.

# Hint: Use the isdisjoint() method, which returns True if sets have no elements in common.
# Sample data:
# s1 = {11, 22, 33}
# s2 = {44, 55, 66}
# Expected Output: True

s1 = {11, 22, 33}
s2 = {44, 55, 66}
print(s1.isdisjoint(s2))

