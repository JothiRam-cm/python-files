# for x in range (50,71):
#     print(x)
#produt of list
# l=[1,2,3,4,5,6,7,8.9]    
# x=1
# for i in l:
#    x*=i 
# print(x)   
   
#    multipication table
x=int(input("enter a number for table other than 1 : "))
assert x>1,"wrong number"
for i in range(1,11):
    if i==2:
        continue
    if i==10:
        break
    y=i*x
    print("{} X {} = {}".format(i,x,y))