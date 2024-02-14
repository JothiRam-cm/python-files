from functools import reduce
l=[1,2,3,4,5]
r=reduce(lambda x,y:x+y,l)
print(r)