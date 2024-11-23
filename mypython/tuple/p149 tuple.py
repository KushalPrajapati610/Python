#6. Write a Python program to check whether an element exists within a tuple.

# Hint: Use the in keyword to check if an element is present in a tuple.

# Sample data:
# t1 = (11, 22, 33, 44, 55)
# Enter value for search: 44
# Expected Output: Yes, 44 is there

no = int(input("Enter the number = "))
t1 = (11, 22, 33, 44, 55)
list1 = list(t1)

if no in list1:
    print("yess")
else:
    print("no")