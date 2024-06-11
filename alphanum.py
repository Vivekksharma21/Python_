# WAP to separate and print the numbers and their position in a given string.

import re
num=input("Enter string containing number:")
pattern="\d+"
res=re.findall(pattern,num)
print("Number in the given string is: ",res)
for i in range(len(res)):
    print("The index positin of number (",res[i],")is:",num.index(res[i]))
