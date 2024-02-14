import re
str="I AM JothiRam".lower()
 # search() method
result=re.search( r'j\w\w\w\w\w\w\w',str )
print(result.group())
print("\n<#------JR------#>\n")

 # Findall() method 
fr=re.findall(r'a',str)
print(fr)
print("\n<#------JR------#>\n")

# match() method #
  # [ it only check the starting of the string ]
mr=re.match(r'i\s\w\w',str) 
print(mr)
print(mr.group())
print("\n<#------JR------#>\n")

# sub() method 
   # you can slice a sub string
   # you can replace the sub string 
sr=re.sub(r'jothiram','GOD',str)
print(sr)    
print("\n<#------JR------#>\n")

# split() method
splitresult=re.split(r'\s',str)
print(splitresult)
print("\n<#------JR------#>\n")

# Quantifiers [+,*,?,{m},{m,n}]
print("re with quantifires\n")
fr=re.findall(r'a\w{1}',str)
print(fr)
print("\n<#------JR------#>\n")
 
 