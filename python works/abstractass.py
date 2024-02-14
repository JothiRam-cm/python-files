from abc import abstractmethod,ABC



class TouchScreenLaptop(ABC):
    name="Touch series"
    
    def __init__(self):
    
     @abstractmethod
     def scrol():
        pass
    @abstractmethod
    def Click():
        pass
    
class HP(TouchScreenLaptop):
     def __init__(self,cruiseControlEnambled,name):
           self.name=name 
           self.cruiseControlEnabled=cruiseControlEnambled
     def display(self):
                print(super().name)
                print("laptop model :{}".format(self.name))     
     def scrol(self):
         print("scrolling in HP")
         
     def Click(self):
         print("click to Hp")    
        
         
class dell(TouchScreenLaptop):
    def __init__(self,cruiseControlEnambled,name): 
           self.cruiseControlEnabled=cruiseControlEnambled
           self.name=name
    def display(self):
                print(super().name)
                print("laptop model :{}".format(self.name))
                
    def scrol(self):
         print("scrolling in dell")
         
    def Click(self):
         print("click to dell")           
         
h=HP(True,"HPNOTEBOOK")
h.display()
h.Click()
h.scrol()
d=dell(True,"DellNoteBook")         
d.display()
d.scrol()
d.Click()         
#t=TouchScreenLaptop("touch series")