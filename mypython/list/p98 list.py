#Write a Python program to print whether the values in a list are odd or even.
#Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]

list = [11, 44, 500, 22, 99, 77, 200, 66, 2]
for i in list:
    if i % 2 == 0:
        print(i , "= even")
    else:
        print(i, "= odd")
