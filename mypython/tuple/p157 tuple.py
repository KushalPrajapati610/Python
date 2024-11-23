#14. Write a Python program to count the occurrences of an item in a tuple.

# Hint: Use the count() method to find how many times an element appears.

# Sample data:
# t1 = (11, 22, 33, 44, 33, 22, 33)
# Enter value to count: 33
# Expected Output: 3

t1 = (11, 22, 33, 44, 33, 22, 33)
list1 = list(t1)
x = list1.count(33)
print(x)
