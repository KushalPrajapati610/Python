#28. Write a Python program to find all unique elements from a list.

#Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

#Expected Result: [44, 500, 99, 77, 200, 66, 2]

list1 = [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]
list1.remove(11)
list1.remove(22)
print(list1)