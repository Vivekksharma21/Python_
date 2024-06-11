# wap to write a python dicitionary to a CSV file. After writing the CSV file read the CSV file and display the contents

import csv
with open('dictcsv.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(["key","values"])
    d=eval(input('Enter a dictionary values :'))
    key=d.keys()
    k=[]
    value=d.values()
    v=[]
    for i in key:
        k.append(i)
    for i in value:
        v.append(i)
    for i in range(len(k)):
        w.writerow([k[i],v[i]])
print('Data written in the successfully')


v=open("dictcsv.csv",'r')
r=csv.reader(v)
data=list(r)
for j in data:
    print(str(j))
v.close()