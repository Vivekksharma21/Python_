# wap to connect with the database and alter the tables student and create one more column to the student table like"result"

import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='vivek2',user='root',password='@Vivek21')
    cursor=con.cursor()
    sql="Alter table Student add column result varchar(10)"
    cursor.execute(sql)
    print("Records updated successfully")
    con.commit()
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("There is a problem with  Sql :",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
