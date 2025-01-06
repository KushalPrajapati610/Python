students={1:"Ram", 22:"Jayul", 3:"Rahul",44:"Anjali",50:"Riya",12:"Hiral",33:"Karan"}

keys = students.keys()
values = students.values()

print(keys)
print(values)




students={1:"Ram", 22:"Jayul", 3:"Rahul",44:"Anjali",50:"Riya",12:"Hiral",33:"Karan"}
students.pop(22)
print(students)
students.popitem()
print(students)
del students[44]
print(students)
students.clear()
print(students)





students={1:"Ram", 22:"Jayul", 3:"Rahul",44:"Anjali",50:"Riya"}
print(students)

students[33]="Hiral"
print(students)

students.setdefault(101,"Sita")
print(students)

students.setdefault(102,"")
students[102]="Ravan"
print(students)





cubes={1: 1, 2: 8, 3: 27}
cubes1={4:64, 5:125}

cubes.update(cubes1)

print(cubes)
