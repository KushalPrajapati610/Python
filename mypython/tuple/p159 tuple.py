#16. Write a Python program to find the largest and smallest items in a tuple.

# Hint: Use the max() and min() functions.

# Sample data:
# t1 = (11, 22, 33, 44, 55)
# Expected Output:
# Max: 55
# Min: 11

t1 = (11, 22, 33, 44, 55)
list1 = list(t1)
x = max(list1)
y = min(list1)
print(x , y)
