text=(input("enter the sentece to slice : ").lower())
result=[x for x in text]

count=[x for x in range(0,len(result)) if result[x]=='a']
# print(count)
# print(result)
s1=[]
for i in range(count[0],count[(len(count)+1)]):
    s1.append(result[i])
# print(s1)
s="".join(s1)
print(s)