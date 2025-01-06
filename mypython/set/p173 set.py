# 4. Write a Python program to remove an item from a set if it is present.

# Hint: Use the discard() or remove() method to remove an element.
# Sample data: {11, 22, 33, 44, 55}
# Enter value: 33
# Expected Output: {11, 22, 44, 55}

no = int(input("Enter the number ="))
set = {11, 22, 33, 44, 55}
set.remove(no)
print(set)
