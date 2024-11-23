#22. Write a Python program to remove empty strings from a list.

#Sample List: ["Raj", "", "Rahul", "Mansi", "", "Manav", "Disha"]
#Expected Result: ["Raj", "Rahul", "Mansi", "Manav", "Disha"]

#Hint: Use a loop .

list1 = ["Raj", "", "Rahul", "Mansi", "", "Manav", "Disha"]

for  x in list1:
    if len(x)==0:
        list1.remove(x)

print(list1)