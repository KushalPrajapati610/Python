#23. Write a Python program to calculate the product of all items in a list.
#Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]
#Expected Result: 453752160000

list1 = [11, 44, 500, 22, 99, 77, 200, 66, 2]
t = 1
for i in list1:
    t = t*i
print(t)