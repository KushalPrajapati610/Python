#32. You have a list of your favourite desserts.

#desserts = ['cheesecake', 'brownie', 'ice cream', 'tiramisu', 'pavlova']

#Using this list, find out:



#1.	How many desserts do you have in your list?
desserts = ['cheesecake', 'brownie', 'ice cream', 'tiramisu', 'pavlova']
print(len(desserts))


#2.	Add 'macaron' at the starting  of the list and show it.
desserts = ['cheesecake', 'brownie', 'ice cream', 'tiramisu', 'pavlova']

desserts.insert(0, 'macaron')
print(desserts)


#3.	You want 'ice cream' to be left after 'pavlova'. Remove it from the end and add it at the correct position.
desserts = ['macaron', 'cheesecake', 'brownie', 'ice cream', 'tiramisu', 'pavlova']
desserts.remove("pavlova")
print(desserts)
desserts.append("ice cream")
print(desserts)