alphabet='abcdefghijklmnopqrstuvwxyz'
def pangram(s):
    for c in alphabet:
     for x in s:
        if c not in s:
            return False
        else: return True
s=input("enter a string to check :")
if(pangram(s)==True):
    print("'{}' is pangram!".format(s))
else:print("'{}' is not pangram!".format(s))                