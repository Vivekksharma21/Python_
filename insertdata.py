#wap to connect with the database and insert details of 10 students using user input to the table Student and print the details after insert

import mysql.connector
try:
    con = mysql.connector.connect(host='localhost',database='vivek2',user='root',password='@Vivek21')
    cursor=con.cursor()
   # cursor.execute("create table Student(sroll varchar(50) primary key,sname varchar(10),sbranch varchar(10),ssem varchar(10),sfees double(10,2))")
    #print("Table Created...")
    num = int(input("Enter number of students : "))
    for i in range(num):
              print("Enter deatails of ",i,"student")
              sroll=input("Enter student roll :")
              sname=input("Enter student name :")
              sbranch=input("Enter student branch : ")
              ssem=input("Enter semester : ")
              sfees=input("Enter fees : ")
              sql = "insert into student(sroll,sname,sbranch,ssem,sfees)VALUES(%s,%s,%s,%s,%s)"
              records=[sroll,sname,sbranch,ssem,sfees]
              cursor.execute(sql,records)
    con.commit()
    print("Records Inserted Successfully...")
    cursor.execute("select * from student")
    data = cursor.fetchall()
    for row in data:
        print("Student roll : ", row[0])
        print("Student name : ", row[1])
        print("Student branch: ",row[2])
        print("Semester :",row[3])
        print("Fees : ",row[4])
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
