students={1:"Ram", 2:"Jayul", 3:"Rahul",4:"Anjali",5:"Riya"}

marks={1:22,2:33,3:16,4:39,5:45}

print(students)
print(marks)



marks={1:22,2:33,3:16,4:39,5:45,4:45, 4:55}

print(marks)



students={}
students[1]="Ram"
students[22]="Jayul"
students[3]="Rahul"
students[44]="Anjali"

print(students)




students={1:"Ram", 22:"Jayul", 3:"Rahul",44:"Anjali",50:"Riya"}

print(students[22])

print(students.get(44))





students={1:"Ram", 22:"Jayul", 3:"Rahul",44:"Anjali",50:"Riya",12:"Hiral",33:"Karan"}

for key,value in students.items():
    print(key,value)
