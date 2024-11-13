# 1= odd , 2 = even,..

no = int(input("enter the limits ="))
for i in range (1, no+1):
    if i % 2 == 0:
        print(i,"= even")
    else:
        print(i,"= odd")
