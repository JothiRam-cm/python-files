def decor(n):
    def inner():
        r=n()
        return r*2
    return inner
def num():
    return 5

fr=decor(num)  
print(fr())