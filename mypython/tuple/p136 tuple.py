#Append
'''
tupleD=(11,22,33,44,55,11,99,33)
tupleD.append(101)
print(tupleD)
'''


tupleD=(11,22,33,44,55)
list1=list(tupleD)
list1.append(101)
tupleD =tuple(list1)
print(tupleD)
