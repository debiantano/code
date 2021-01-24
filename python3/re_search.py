 import re

 txt="The rain in Spain"
 x=re.search("^The.*Spain$",txt)

 print(x)
 if x:
     print("Yes")
 else:
     print("no match")
