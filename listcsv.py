#wap to write a python list of lists to a csv file . After writing the csv  file read the CSV file and display the contents.'''

import csv
with open("student1.csv","w") as f:
    w=csv.writer(f)
    list1=eval(input("Enter the list:"))
    w.writerow(list1)
print("Data written successfully...")

with open("student1.csv",'r') as v :
    data = csv.reader(v)
    read=list(data)
    print(read)
