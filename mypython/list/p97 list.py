#Write a Python program to print only even values from a list.
#Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]


list1 = [11, 44, 500, 22, 99, 77, 200, 66, 2]
for i in list1:
    if i % 2 == 0:
         print(i, end=" ")
