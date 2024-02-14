#factorial
n=int(input("enter a number : "))
def f(n):
    if n==0:
        r=1
    else:
     r=n*f(n-1)
    return r  
print(f(n))    