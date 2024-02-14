# from curses import doupdate
from datetime import*

def validate(expdate):
    if(expdate>datetime.now().date()):
        return 'valid'
    else:
        raise RuntimeError("card has expired !!")
    
print(validate(date(2023,12,31)))        