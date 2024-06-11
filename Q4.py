'''WAP to search a literal string in a string and also find the location within the original string where the pattern occurs.
Sample text:'The quick brownn fox jumps over the lazy dog'
Search word:'fox'  '''

import re
x='The quick brown fox jumps over the lazy dog'
result=re.search("fox",x)
if result:
    print("Literal string found in the string and the location is:",x.index("fox"))
else:
    print("Literal string not found in the string")