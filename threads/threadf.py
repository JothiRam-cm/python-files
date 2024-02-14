from threading import *
from time import *

def EvenNumbersThread():
        print(current_thread().getName())
        for i in range(1,101): 
            if i%2==0:print(i,end=" ")
        print()    
         
def OddNumbersThread():
        print(current_thread().getName())
        for i in range(1,101): 
            if i%2!=0:print(i,end=" ")  
        print()     
          
t1=Thread(target=EvenNumbersThread)
t2=Thread(target=OddNumbersThread)
t1.start()
t2.start()            