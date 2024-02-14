# n=int(input("Enter a number : "))
# i=0
# while i<=n:
#  if i%10!=0:print(i)
#  i+=1 
 
n1=int(input("enter a number : "))
prime=True
for i in range (2,n1-1):
    if n1%i==0:prime=False
if prime==False:
    print("it's not a prime number")    
else:print("it's a prime number")    


