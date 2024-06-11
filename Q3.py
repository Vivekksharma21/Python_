# WAP to search for numbers(0-9) of length between 1 and 3 in a given string.
import re
x=input("Enter a string containing number:")
pattern='\d+'
test_number=x
result=re.findall(pattern,test_number)
for i in range(len(result)):
    if len(result[i])<=3:
        print(result[i])
    else:
        pass