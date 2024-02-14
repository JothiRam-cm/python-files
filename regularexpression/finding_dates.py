import re
str="my birth day 5-10-2003,my father DOB 5-6-1972,my mother DOB 16-9-1088,my sister DOB 16-11-2005,my brother DOB 28-5-2007"
dr=re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(dr)
print("\n<#------JR------#>\n")