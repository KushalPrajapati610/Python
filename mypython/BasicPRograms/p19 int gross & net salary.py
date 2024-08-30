salary=int(input("enter the salary="))
ma= 0.10 * salary
da = 0.52 * salary
ltc= 0.05 * salary
hra= 0.10 * salary
va= 0.10 * salary
print("ma =",ma)
print("da =",da)
print("ltc =",ltc)
print("hra =",hra)
print("va =",va)
Grosssalary= salary + ma + da + ltc + hra +va
Netsalary= Grosssalary - 1000 #-1000 is PF
print("Grosssalary =",Grosssalary)
print("Netsalary =",Netsalary)