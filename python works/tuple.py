#() it is optional
#immutable
#notchanging
#can be used as keyword
l=[6,7,8,9,0]
tp=(1,2,3,4,5,'jothiram')
print(type(tp))
print(tp.count(2))
tp1=tuple(l)
print(tp1)

###set
s={1,2,3,4,5,'jothiram'}

####student 

student={'jothi':['python','java'],'ram':['c','c++']}
keys=student.keys()

for i in keys:
    print("course taken by",i,"are:")
    for ec in student[i]:
        print("<>",ec)