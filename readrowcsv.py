# WAP to read each row from a given csv file and print a list of strings.
import csv
name=input("Enter file name:")
f=open(name,'r')
r=csv.reader(f)
data=list(r)
for i in range(len(data)):
    r1=data[i]
    print(r1)