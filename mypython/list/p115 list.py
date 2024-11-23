#Write a Python program to check if the first and last numbers in a list are the same.
#Sample List 1: [100, 200, 320, 40, 100]
#Sample List 2: [751, 6, 3, 5, 9]
#Expected Result: True for the first list, False for the second list
#Hint: Compare list[0] with list[-1] to check if the first and last numbers are the same.

list1 = [100, 200, 320, 40, 100]
list2 = [751, 6, 3, 5, 9]

first = list1[0]
last = list2[-1]

if first == last:
    print("True for the first list")
else:
    print(" False for the second list")