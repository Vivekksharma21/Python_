# wap to read specific columns of a given CSV file and print the contents of the columns
import csv
v = open('student.csv','r',newline='')
r=csv.reader(v)
data = list(r)
r = data[0]
col=input("Enter column name : ")
row=r.index(col)
for i in range(len(data)):
   r=data[i]
   if(data[i][row]==''):
      pass
   else:
      print(data[i][row])
v.close()