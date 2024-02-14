m,p,c=[int(x) for x in input("Enter the marks: ").split()]
avgm=(m+p+c)/3
if avgm>=35:
    if (avgm>=59)&(avgm<=69):print("you got 'C' grade")
    elif (avgm>69)&(avgm<=79):print("you got 'B' grade")
    elif(avgm>79):print("you got 'A' grade")
    else:print("you have passed")
else:print("beter luck next time")    
print("your average:",avgm)