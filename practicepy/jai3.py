n=int(input("enter a start value : "))
m=int(input("enter  a end value : "))
if m < n :
    n,m = m,n
for i in range(n,(m+1)):
    x=[]
    while i!=0:
        x.append(str(i%10))
        i=int(i/10)
    y="".join(x)
    x=y[::-1]    
    if x==y:
      print("real numer-{} <::::> mirror number-{}".format(x,y))

    