
class invalidPassword(Exception):
    def __init__(self,info) -> None:
        self.info=info
def passwordchecking(pas):
    if(len(pas)<8):raise invalidPassword("you password is less than 8 characters!".upper())
    elif(len(pas)>8):raise invalidPassword("your password is greater than 8 character!".upper())
    else:print("password is correct!!".upper())

passwordchecking(input("enter the password : ".upper()))    