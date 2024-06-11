# wap to connect with the database and delete the details of the student whose fees is below 3000

import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='vivek2',user='root',password='@Vivek21')
    cursor=con.cursor()
    sql="delete from  student where sfees<=%f"
    cursor.execute(sql %(20000))
    print("Records updated Successfully")
    con.commit()
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("There is a problem with sql :",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
