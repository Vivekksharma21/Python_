# WAP to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
import re
date=input("Enter the date in this yyyy-mm-dd format:")
pattern='\d+'
s=re.findall(pattern,date)
s[0],s[-1]=s[-1],s[0]
for i in s:
    merge="-".join(s)
print("After conversion of (",date,")in this dd-mm-yyyy format :",merge)