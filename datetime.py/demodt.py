import time,datetime 
epochseconds=time.time()
t=time.ctime(epochseconds)
print(t)
print("\n<----JR---->\n")

dt=datetime.datetime.today()
print("Current Date : {}/{}/{}".format(dt.day,dt.month,dt.year))
print("Current Time : {}:{}:{}".format(dt.hour,dt.minute,dt.second))
print("\n<----JR---->\n")

from datetime import*
d=date(2023,10,23)
ti=time(8,25,20)
dti= datetime.combine(d,ti)
print(dti)
print("\n<----JR---->\n")