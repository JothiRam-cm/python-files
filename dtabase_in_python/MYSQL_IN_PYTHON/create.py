import mysql.connector;

conn=mysql.connector.connect(host='localhost',database='JRDB',user='root',password='My_05102003')
if conn.is_connected():print("<< connected to database JRDB >>".upper())
cursor=conn.cursor()

try:
    cursor.execute('insert into anime values(6,"HELL''S PARADISE","SEARCHING FOR CCELASTIAL_DRINK")')
    conn.commit()
    print("< < Added New Record > >")
except:
    conn.rollback()

cursor.execute('select * from anime')

rows=cursor.fetchall()

print("Number of records ".upper(),cursor.rowcount)

print("\n\t\t< < Displaying Records > >\n")
for row in rows:
    print("\t",row,"\n") 

cursor.close()     

conn.close()    