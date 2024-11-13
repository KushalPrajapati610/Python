no = int(input("Enter the limits ="))
div = int(input("Enter div no. ="))
c = 0
for i in range(1, no+1):
    if i % div == 0:
        print(i)
        c=c+1
print("Count = ", c)
