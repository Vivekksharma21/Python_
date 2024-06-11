import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="@Vivek21",database="collage")
cursor=conn.cursor()
cursor.execute("create table student(roll varchar(10) primary key,name varchar(20))")
cursor.execute("insert into student values('1','Deba')")
st_insert=("insert into student (roll,name) values(%s,%s)")
values=(("4","Rahul"),("5","Rohan"))
cursor.executemany(st_insert,values)
conn.commit()
cursor.execute("select * from student")
for i in cursor:
    print(i)