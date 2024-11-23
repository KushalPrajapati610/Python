#Write a Python program to change the sign of elements in a list.
#Sample List: [11, -44, 500, -22, -99, -77, 200, -66, 2]

list = [11, -44, 500, -22, -99, -77, 200, -66, 2]
for i in list:
    if i < 0:
        print(-i, end=", ")
    else:
        print(-i, end=", ")