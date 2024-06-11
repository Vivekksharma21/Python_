# wap to read a given CSV FILE having tab delimiter

'''import csv
with open("student.csv",'w',newline='') as v :
    w=csv.writer(v)
    w.writerow(["Roll no."," Name"," Branch"," Registration no."])
    n = int(input("Enter no. of students : "))
    for i in range(n):
        roll = input("Enter student roll no. : ")
        name = input("Enter student name : ")
        branch = input("Enter student branch : ")
        regis = input("Enter registration no. of student : ")
        w.writerow([roll,name,branch,regis])
    print("Total student data written to csv file successfully ")'''

import csv
f=open("student.csv",'r')
r=csv.reader(f)
data = list(r)
#print(data)
for line in data:
    for word in line:
        print(word,'\t',end="\t")
    print()

