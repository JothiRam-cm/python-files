def vowelscounter():
    s=input("Enter a string : ")
    vowels="aeiou"
    count=0
    for x in vowels:
      for y in (s.lower()):
        if x in y:
            count+=1
        else:continue
    print("The no of vowels in {} is {}".format(s,count))     
vowelscounter()           