held=int(input("Number of classes held="))
attended=int(input("Number of classes attended="))

if attended>75:
    percentage =held/attended*100
    print("percentage=",percentage)
    print("you can give exam")
else:
    print("sorry you can't give exam")