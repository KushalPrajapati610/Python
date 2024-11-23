#11. Write a Python program to reverse a tuple.

# Sample data:
# t1 = (11, 22, 33, 44, 55)
# Expected Output: (55, 44, 33, 22, 11)

t1 = (11, 22, 33, 44, 55)
list1 = list(t1)
list1.reverse()
t1 = tuple(list1)
print(t1)
