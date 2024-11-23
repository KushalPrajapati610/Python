#29. Using the following list of programming languages per paradigm:

#procedural = ["c", "fortran", "pascal"]
#object_oriented = ["java", "c++", "python"]
#functional = ["haskell", "scala", "lisp"]

#Write a program that asks the user to enter a programming language and tells them which paradigm it belongs to.

lang = input("Enter language = ")
list1 = ["c", "fortran", "pascal"]
list2 = ["java", "c++", "python"]
list3 = ["haskell", "scala", "lisp"]
if lang in list1:
    print("procedural")
elif lang in list2:
    print("object_oriented")
elif lang in list3:
    print("functional")
else:
    print("worng language")
