import pickle
f=open("Student.data","rb")
obj=pickle.load(f)
obj.details()