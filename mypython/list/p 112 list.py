#. Write a Python program to take a value from the user and add it at a specified index.
#Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]
#Input: Enter position: 2, Enter value: 999
#Expected Result: [11, 999, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]


list1 = [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]
p = int(input("Enter position= "))
v = int(input("Enter value= "))
list1[p-1]=v
print(list1)