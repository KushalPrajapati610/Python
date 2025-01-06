f1=open("abc", "r")
while True:
    ch=f1.read(1)
    if not ch:
        break
    if ch==" ":
        pass
    else:
        print(ch,end="")
f1.close()

"""
1) upper? lower?
2) vowel?
3) upper X
4) vowel X
5) upper 9
"""