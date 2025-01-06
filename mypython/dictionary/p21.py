import random

d1 = {}

n = int(input("Enter limit =>"))
for i in range(1, n + 1):
    k = i
    v = random.randint(1, 30)
    d1[k] = v

c = 0
c1 = 0
for key, values in d1.items():
    if values >= 18:
        print(key, "\t", values, "=", "pass")
        c = c + 1
    else:
        print(key, "\t", values, "=", "fail")
        c1 = c1 + 1
print("Count of pass= ", c)
print("Count of fail=", c1)
