#4. Write a Python program to add an item in a tuple.

# Hint: Tuples are immutable, so to add an item, convert the tuple to a list, add the item, then convert it back to a tuple.

# Sample data:
# t1 = (11, 22, 33, 44, 55)
#Enter data: 100
#Expected Output: (11, 22, 33, 44, 55, 100)

t1 = (11, 22, 33, 44, 55)
list1 = list(t1)
list1.append(100)
t1 = tuple(list1)
print(t1)
