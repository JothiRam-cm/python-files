prime=True
l1 =[int (x) for x in (input("enter the numbers : ").split(" ")) ]
print("\nGiven n+1 list : ",l1)
p,m=1,min(l1)
for i in l1: p=p*i
s=p+m 
for i in range (2,s-1):
    if s%i==0:prime=False 
if prime==False:print("\n{} is not a prime number\n".format(s))    
else:print("\n{} is a prime number\n".format(s))