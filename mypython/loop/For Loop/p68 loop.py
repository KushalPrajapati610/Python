no = int(input("Enter the limits ="))
div = int(input("Enter div no. ="))

for i in range(1, no + 1):
    if i % div == 0:
        print(i)
