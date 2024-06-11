# WAP to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
import re
x=input("Enter the date in yyyy-mm-dd format:")
pattern='\d+'
s=re.findall(pattern,x)
s[0],s[-1]=s[-1],s[0]
for i in s:
    s1="-".join(s)
print("After conversions:",s1)