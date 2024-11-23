#8. Write a Python program to remove an item from a tuple.

# Hint: Since tuples are immutable, convert the tuple to a list, remove the item, then convert it back to a tuple.

# Sample data:
# t1 = (11, 22, 33, 44, 55)
# Enter value for delete: 22
# Expected Output: (11, 33, 44, 55)

no = int(input("Enter the number ="))
t1 = (11, 22, 33, 44, 55)
list1 = list(t1)
list1.remove(no)
t1 = tuple(list1)
print(t1)
