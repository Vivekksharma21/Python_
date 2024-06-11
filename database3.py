import mysql.connector
try:
    con = mysql.connector.connect(host='localhost',database='vivek2',user='root',password='@Vivek21')
    cursor=con.cursor()
    #cursor.execute("create table employee(eno int(5) primary key,ename varchar(10),esal double(10,2),eaddr varchar(10))")
    print("Table Created...")
    sql = "insert into employees(eno,ename,esal,eaddr)VALUES(%s,%s,%s,%s)"
    records=[(1100,'sachin',1000,'Mumbai'),
             (200,'Dhoni',2000,'Ranchi'),
             (300,'Virat',3000,'Delhi')]
    cursor.executemany(sql,records)
    con.commit()
    print("Records Inserted Successfully...")
    cursor.execute("select * from employees")
    data = cursor.fetchall()
    for row in data:
        print("Employee Number : ",row[0])
        print("Employee name : ",row[1])
        print("Employee salary : ",row[2])
        print("Employee address :",row[3])
        print()
        print()
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("There is a problem with sql : ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
