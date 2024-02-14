def cusgen(x,y):
    while(x<y):
        yield x
        x+=1
r=cusgen(22,56)
for i in r:print(i,end=" ")        
