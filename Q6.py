#6.WAP to separate and print the numbers and their position in a given string.
import re
x=input("Enter a number containig number:")
pattern="\d+"
result=re.findall(pattern,x)
# print(result)
for i in range(len(result)):
    print("The index positin of ",result[i],"is:",x.index(result[i]))
