#5. Write a Python program to get the 4th element from last of a tuple.

# Hint: You can access tuple elements using positive and negative indices.

# Sample data:
# t1 = (11, 22, 33, 44, 55)
# Expected Output: 44 (for both 4th element and 4th from last)

no = int(input("Enter the number ="))
t1 = (11, 22, 33, 44, 55)
list1 = list(t1)
x = list1[no]
y = list1[-no]
print(x)
print(y)
