#3. Write a Python program to create a tuple with numbers and print one item.

# Hint: You can access tuple elements using their index, starting from 0.

# Sample data:
# t1 = (11, 22, 33, 44, 55)
# index=int(input("Enter index =>"))
#Expected Output: 33 (for printing the 3rd item)

index=int(input("Enter index = "))
t1 = (11, 22, 33, 44, 55)
list1 = list(t1)
x = list1[index]
print(x)
