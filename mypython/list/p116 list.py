#21. Write a Python program to square each element in a list.

#Sample List: [11, 2, 4, 3, 6, 7]

#Expected Result: [121, 4, 16, 9, 36, 49]

#Hint: Use a loop or list comprehension to square each number using number ** 2.

list1 = [11, 2, 4, 3, 6, 7]
for i in list1:
    print(i*i,end=", ")