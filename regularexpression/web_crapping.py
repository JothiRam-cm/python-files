import re
import urllib.request 

sites=["google.com","baraththippireddy.com"]

for s in sites:
    print("searching "+s)
    response=urllib.request.urlopen("http://"+s)
    text=response.read()
    title=re.findall("<p>.*</p>",str(text),re.I)
    print(title[1::])         