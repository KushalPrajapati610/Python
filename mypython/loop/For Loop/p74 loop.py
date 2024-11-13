no = int(input("Enter limits ="))

for i in range(1, no+1):
    if i % 2 == 0:
        print(i*i, end=" + ")
    else:
        print(i*i*i, end=" + ")
        