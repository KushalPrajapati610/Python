#Write a Python program to remove even numbers from a list.
#Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]

list1 = [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]
for i in list1:
    if i % 2 != 0:
        print(i, end=", ")
    # else:
    #     print(i, end=", ")
    #