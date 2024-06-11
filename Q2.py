#2.WAP to match a string that contains only upper and lowercase letters,numbers and underscores. 
import re
x=input("Enter a word containing upper,lower and uhnder scores:")
pattern='\w'
test_string=x
if re.search(pattern,test_string):
    print("Search successful")
else:
    print("Search unsuccessful")

