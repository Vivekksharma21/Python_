# wap that matches a word containing 'z', not the start or end of the word
import re
str1 = input("Enter a sentence :")
pattern = '\Bz\B'

if re.search(pattern,str1):
    print( 'Z found in the text ')
else:
    print ('z not found in the text ')
