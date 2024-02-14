def decofun(fun):
   def inner(n):
        x="how are you"
        r=fun(n) +x 
        return r
   return inner 

@decofun
def hi(name):
   return "Hi "+name
 
print(hi("JR "))    
