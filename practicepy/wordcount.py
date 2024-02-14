import re
sentence=input("enter a sentence : ")
words= re.findall(r"\w+",sentence)
print("Number of words in the give sentence is :",len(words))