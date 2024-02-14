s=input("enter a string : ")
charcount={}
for x in s:
    if x in charcount.keys():
        charcount[x]+=1
    else:
        charcount[x]=1     
for y,z in (charcount.items()):
        print("{} is present {} times".format(y,z))        