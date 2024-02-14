import pickle,Student
f=open("Student.data","wb")
s=Student.Student(3,"jothiram",80)
pickle.dump(s,f) 