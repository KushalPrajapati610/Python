#Display only numbers divisible by 7 , count and sum it
tupleD = (11, 21, 33, 49, 55, 11, 99, 33)
c = 0
for i in tupleD:
    if i % 7 == 0:
        print(i)
    c = c + i
print(c)