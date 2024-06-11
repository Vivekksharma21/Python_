# wap to connect with the database and add a fine of 1000 to the students whose fee is greater than 50000


import mysql.connector
try:
    con=mysql.connector.connect(host='localhost',database='vivek2',user='root',password='@Vivek21')
    cursor=con.cursor()
    sql="update student set sfees=sfees+%f where sfees>%f"
    cursor.execute(sql %(1000, 50000))
    print("Records are updated Successfully")
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
