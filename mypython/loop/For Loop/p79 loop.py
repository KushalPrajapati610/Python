#1 + 3 + 5 +7 = 16

no = int(input("Enter limits ="))
t = 0
for i in range(1, no+1):
    print(i*i, end=" + ")
    t=t + i * i
print(t, end="")
