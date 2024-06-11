import mysql.connector
try:
    con=con = mysql.connector.connect(host='localhost',database='vivek',user='root',password='@Vivek21')
    cursor = con.cursor()
    increment=float(input("Enter Increment salary : "))
    salrange = float(input("Enter salary range : "))
    sql="update employee set esal=esal+%f where esal<%f"
    cursor.execute(sql%(increment,salrange))
    print("Records updated successfully")
    con.commit()
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("There is a problem with sql : ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    
