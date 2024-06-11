# wap to create another table and copy the content of employee table from the database

import mysql.connector
try:
    con = mysql.connector.connect(host='localhost',database='vivek',user='root',password='@Vivek21')
    cursor=con.cursor()
    cursor.execute("select*from employee")
    data = cursor.fetchall()
    list=[]
    for row in data:
        t=(row[0],row[1],row[2],row[3])
        list.append(t)
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("There is a problem with MySql: ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

try:
    con = mysql.connector.connect(host='localhost', database='vivek', user='root', password='@Vivek21')
    
    cursor=con.cursor()

    cursor.execute("create table employee1(eno int(5) primary key,ename varchar(10),esal double(10,2),eaddr varchar(10))")
    sql = "insert into employee1(eno,ename,esal,eaddr)VALUES(%s,%s,%s,%s)"
    cursor.executemany(sql,list)
    con.commit()
    print("Records copied from MySql database to mysql database successfully ")
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("There is a problem with sql ",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
