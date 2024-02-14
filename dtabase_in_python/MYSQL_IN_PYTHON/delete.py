import mysql.connector;

conn=mysql.connector.connect(host='localhost',database='JRDB',user='root',password='My_05102003')
if conn.is_connected():print("<< connected to database JRDB >>".upper())

def Delete(id):
    cursor=conn.cursor()
    st="delete from anime where id='%d'"
    arg=(id)
    try:
        cursor.execute(st % arg)
        conn.commit()
        print("< < Deleted a Record > >")
    except:conn.rollback()
    finally:
        cursor.execute('select * from anime')
        rows=cursor.fetchall()
        print("Number of records ".upper(),cursor.rowcount)
        print("\n\t\t< < Displaying Records > >\n")
        for row in rows:
            print("\t",row,"\n") 
        cursor.close()
        conn.close() 
Delete(int(input("Enter Id to Delete:: ")))
    