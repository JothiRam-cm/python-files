p=float(input("enter the principal amount : "))
r=float(input("enter the rate of intrest : "))
t=float(input("enter time period (years) : "))
a=p*((1+(r/100))**t)
CI=a-p
print("compout intrest for the amount {} is {}".format(p,CI))
