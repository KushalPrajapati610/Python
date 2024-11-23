#25. Write a Python program to count the number of even and odd numbers in a list.

#Sample List: [11, 44, 500, 22, 99, 77, 200, 66, 2]
#Expected Result:

#Even numbers: 6
#Odd numbers: 3

#Hint: Use a loop and the modulus operator % to check if each number is even or odd.

list1 = [11, 44, 500, 22, 99, 77, 200, 66, 2]
t = 0
t1 = 0
for i in list1:
    if i % 2 == 0:
        print(i)
        t = t+1
    else:
        print(i)
        t1 = t1+1
print("even count =", t)
print("odd count =", t1)