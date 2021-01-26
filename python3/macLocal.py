
#!/usr/bin/python3
import re
from re import findall
from subprocess import check_output

output=check_output(['ifconfig', 'eth0']).decode()
#print(output)

x = re.split("\s", output)
#print(type(x))

sin_strings=[]

for string in x:
	if(string!=""):
		sin_strings.append(string)

print(sin_strings[5])
