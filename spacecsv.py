# wap to read a given CSV file with initial spaces after a  delimiter and remove those initial spaces

import csv
with open('student.csv', 'r') as v:
   data = csv.reader(v,skipinitialspace=True)
   for row in data:
     print(','.join(row))