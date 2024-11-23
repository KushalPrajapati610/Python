#17. Write a Python program to sort a tuple of numbers in ascending order.

# Hint: Convert the tuple to a list, sort the list, and convert it back to a tuple.

# Sample data:
# t1 = (55, 22, 33, 11, 44)
# Expected Output: (11, 22, 33, 44, 55)

t1 = (55, 22, 33, 11, 44)
list1 = list(t1)
x = list1.sort()
t1 = tuple(list1)
print(t1)

