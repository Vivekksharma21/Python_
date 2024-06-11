# WAP to abbreviate 'Road' as 'Rd'. in a given string.


import re
list1=[]
x=input("Enter a string:")
pattern="\s"
r=re.split(pattern,x)
for i in r:
    list2=i[0]+i[-1]
    list1.append(list2)
list3=' '.join(list1)
print("The resultant string is:",list3)