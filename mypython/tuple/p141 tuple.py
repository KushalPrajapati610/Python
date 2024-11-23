# #Print only even values
# tupleD = (11, 22, 33, 44, 55, 11, 99, 33)
# for i in tupleD:
#     if i % 2 == 0:
#         print(i)
#

#Print Sum of even and Count also
tupleD = (11, 22, 33, 44, 55, 11, 99, 33)
c = 0
for i in tupleD:
    if i % 2 == 0:
        print(i)
    c = c + i
print(c)