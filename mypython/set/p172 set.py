#3. Write a Python program to add member(s) to a set.

# Hint: Use the add() method to add a new element to the set.

# Sample data: {11, 22, 33, 44, 55}

# Enter value: 66

# Expected Output: {11, 22, 33, 44, 55, 66}

no = int(input("Enter the number ="))
set = {11, 22, 33, 44, 55}
set.add(no)
print(set)
