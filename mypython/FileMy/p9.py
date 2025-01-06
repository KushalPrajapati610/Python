#upper 9
f1 = open("abc", "r")
while True:
    ch = f1.read(1)
    if not ch:
        break
    if ch.isupper():
        print(9, end="")
    else:
        print(ch,end="")
f1.close()
