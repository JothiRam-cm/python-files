n=int(input("Enter a nuber to check : "))
prime=False
for x in range(2,n):
    if n%x==0:
        prime=True
        break
if(prime==True):print("{} is not a prime numbeer.".format(n))
else:print("{} is a prime number.".format(n))
