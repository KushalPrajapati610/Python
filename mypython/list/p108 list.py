#Write a Python program to find elements larger than a given value in a list.
#Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

list1 = [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]
for i in list1:
    if i > 50:
        print(i, end=", ")
