n=int(input("Enter a number of employees : "))
employee={}
for i in range(n):
    name=input("Enter employee name : ")
    salary=int(input("Enter the salary of employee : "))
    employee[name]=salary
while True:
    name=input("Enter the employee name : ")
    salary=employee.get(name,0)
    if salary==0:print("No such employee exist : ")
    else: print("The salary of {} is {} ".format(name,salary)) 
    choice=input("Do you want to continue [yes|no]")   
    if choice=="no":break