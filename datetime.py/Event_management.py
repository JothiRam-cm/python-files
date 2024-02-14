from datetime import *

class Event :
    def __init__(self,eventname,eventdate) -> None:
        self.eventname=eventname
        self.eventdate=eventdate
        self.venues=[]
        print(" event name :".upper(),self.eventname)
        print(" event date :".upper(),self.eventdate)
    def addvenue(self,venue):
           self.venues.append(venue)
        
          
class Venues:
    def __init__(self,place,starttime,endtime) -> None:
        self.place=place
        self.starttime=starttime
        self.endtime=endtime
        self.addres=[]
    def addaddress(self,address):
        self.addres.append(address)
            

class Address:
    def __init__(self,street,city,state) -> None:
        self.street=street
        self.city=city
        self.state=state
    
            
event=Event("Journal level sports",date(2023,10,27))
address=Address("kamarajar","madurai","Tamil Nadu")    
venue=Venues("sports courts stadium.",time(8,00),time(2,00))
event.addvenue(venue)
venue.addaddress(address)
for i in venue.addres:
    for j in event.venues:
        print(" Venue Name : {} \n Enent starting Time : {} \n Enent Ending Time : {} ".format(j.place,j.starttime,j.endtime))
    print(" Adress : {} street at {} city in {} state.".format(i.street,i.city,i.state))
           