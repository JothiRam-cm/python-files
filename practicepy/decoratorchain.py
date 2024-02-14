def square(fun):
    def inner():
        r=fun()
        return r**2
    return inner

def cube(fun):
    def inner():
        n=fun()
        return n**3
    return inner

def half(fun):
    def inner():
        n=fun()
        n=int(n/2)
        return n
    return inner


@half
@square
@cube
def num():
    return 2

print(num())
        
    