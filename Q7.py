#7.WAP to abbreviate 'Road' as 'Rd'. in a given string.
import re
r2=[]
x=input("Enter a string:") 
pattern="\s"
r=re.split(pattern,x)
for i in r:
    r1=i[0]+i[-1]
    r2.append(r1)
L=' '.join(r2)
print("The resultant string is:",L)
