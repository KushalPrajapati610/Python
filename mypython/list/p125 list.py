#30. Using following list of cities per country,

#india = ["mumbai", "banglore", "chennai", "delhi"]
#pakistan = ["lahore","karachi","islamabad"]
#bangladesh = ["dhaka", "khulna", "rangpur"]

#Do the following task:

#1.	Write a program that asks user to enter a city name and it should tell which country the city belongs to

"""
con = input("Enter country = ")
list1 = ["mumbai", "banglore", "chennai", "delhi"]
list2 = ["lahore","karachi","islamabad"]
list3 = ["dhaka", "khulna", "rangpur"]
if con in list1:
    print("india")
elif con in list2:
    print("pakistan")
elif con in list3:
    print("bangladesh")
else :
    print("Wrong city")
"""

#2.	Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
# For example if I enter mumbai and chennai, it will print "Both cities are in India" but
# if I enter mumbai and dhaka it should print "They don't belong to same country"

con = input("Enter 1 city = ")
con1 = input("Enter 2 city = ")
list1 = ["mumbai", "banglore", "chennai", "delhi"]
list2 = ["lahore","karachi","islamabad"]
list3 = ["dhaka", "khulna", "rangpur"]
if con in list1 and con1 in list1:
    print("Both cities are in India")
elif con in list2 and con1 in list2:
    print("Both cities are in pakistan")
elif con in list3 and con1 in list3:
    print("Both cities are in bangladesh")
else :
    print("They don't belong to same country")
