#9. Write a Python program to find the index of an item in a tuple.

# Hint: Use the index() method to find the position of an element in a tuple.

# Sample data:
# t1 = (11, 22, 33, 44, 55)
# Enter value to find its index: 22
# Expected Output: 1

no = int(input("Enter the number ="))
t1 = (11, 22, 33, 44, 55)
c = 0
if no in t1:
    list1 = list(t1)
    x = list1.index(no)
    print(x)
else:
    print("sorry")
