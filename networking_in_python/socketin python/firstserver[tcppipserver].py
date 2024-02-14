import socket

host="localhost"
port=4000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
print("server is listening in port : ",port)
s.listen()
c,addr= s.accept()
print("conection from :",str(addr))
c.send(b"hello jothiram")
c.send("hi jothi ram".encode())
c.close()
