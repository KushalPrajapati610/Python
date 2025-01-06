#12.Write a Python program to check if an element is present in a set.

# Hint: Use the in keyword to check if an element exists in the set.
# Sample data: {11, 22, 33, 44, 55}
# Enter value: 22
# Expected Output: True
no = int(input("Enter Value:"))
s1 = {11, 22, 33, 44, 55}
s2 = {no}
print(s1.issuperset(s2))
