#!/usr/bin/python3

lista=[1,2,3,4,"","curl","","arp",""," "]
sin_strings=[]

for i in lista:
	if(i!="" and i!=" "):
		sin_strings.append(i)

print(sin_strings)

