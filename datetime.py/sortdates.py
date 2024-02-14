from datetime import*
import time
starttime=time.perf_counter()
ldates=[]
d1=date(2003,10,5)
d2=date(2005,11,16)
d3=date(2007,5,28)
d4=date(1972,6,5)
d5=date(1988,9,16)
ldates.append(d1)
ldates.append(d2)
ldates.append(d3)
ldates.append(d4)
ldates.append(d5)
ldates.sort() 
time.sleep(5)
for d in ldates:
    print(d)
endtime=time.perf_counter()
print("Execution time :",int(starttime-endtime))    