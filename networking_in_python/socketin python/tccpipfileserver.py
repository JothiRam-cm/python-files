import socket

host="localhost"
port=4000
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
print("server is listening in port : ",port)
s.listen()
c,addr= s.accept()
print("conection from :",str(addr))
filename=c.recv(1024)
try:
    f=open(filename,'+rb')
    content=f.read()
    c.send(content)
    f.close()
except FileNotFoundError :
    c.send(b"File Not Exists..!")
c.close()
