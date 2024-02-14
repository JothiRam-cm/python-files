import mysql.connector;

conn=mysql.connector.connect(host='localhost',database='JRDB',user='root',password='My_05102003')
if conn.is_connected():print("<< connected to database JRDB >>".upper())
cursor=conn.cursor()
cursor.execute('select * from anime')
row=cursor.fetchone
while row is not None:
    print(row)
    row=cursor.fetchone() 

cursor.close()     

conn.close()    