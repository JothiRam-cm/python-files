import mysql.connector;

conn=mysql.connector.connect(host='localhost',database='JRDB',user='root',password='My_05102003')
if conn.is_connected():print("<< connected to database JRDB >>".upper())
cursor=conn.cursor()
cursor.execute('select * from anime')
rows=cursor.fetchall()
print("Number of records ".upper(),cursor.rowcount)
for row in rows:
    print(row) 

cursor.close()     

conn.close()    