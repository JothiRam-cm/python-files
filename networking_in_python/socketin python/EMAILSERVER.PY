import smtplib
from email.mime.text import MIMEText
body="this a testing email"
msg=MIMEText(body)
msg['From']="c.m.2003ram@gmail.com" #c.m.ram2003@gmail.com
msg['To']="c.m.ram2003@gmail.com" #c.m.2003ram@gmail.com
msg['Subject']="testing mail"

server= smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("c.m.2003ram@gmail.com","rkpjllerntrqplvo")
server.send_message(msg) 
print("mesage sent".upper())
server.quit()