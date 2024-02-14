class Student:
    def __init__(self,id,name,score) -> None:
       self.id=str(id)
       self.name=name
       self.score=str(score)
        
    
    def details(self):
        print("ID : " + self.id+"\n"+"Name : " + self.name+"\n"+"Score : " + self.score+"\n")    
        
               