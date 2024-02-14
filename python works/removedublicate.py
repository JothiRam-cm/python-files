s=input("enter a string : ")
temp=[]
for x in s:
    if x not in temp:
        temp.append(x)
print(temp)
s2="".join(temp)
print("after removing dublicates : {} ".format(s2))