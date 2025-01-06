#16. Write a Python program to find the union of multiple sets.

# Hint: Use the union() method or | operator to combine all elements from multiple sets.
# Sample data:
# s1 = {11, 22}
# s2 = {33, 44}
# s3 = {55, 66}
# Expected Output: {11, 22, 33, 44, 55, 66}

s1 = {11, 22}
s2 = {33, 44}
s3 = {55, 66}
print(s1.union(s2) | s1.union(s3))