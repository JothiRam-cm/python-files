s=input("enter a sentence : ")
sl=s.split()
rsl=[]
ewr=[]
i=len(sl)-1
j=0
while i>=0:
    rsl.append(sl[i])
    i-=1
while j<len(sl):
    ewr.append(sl[j][::-1])
    j=j+1
#print("\t",rsl,ewr,"\n")    
frsl=' '.join(rsl)   
fewr=' '.join(ewr)
print("\n\t### Entered string ###\n")
print("\t*",s,"\n")
print("\t### reversing the sentence ###\n")
print("\t*",frsl,"\n")
print("\t### reversing each word of an sentence ###\n")
print("\t*",fewr,"\n")
