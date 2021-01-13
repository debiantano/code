#!/usr/bin/python3

#eliminar elementos vacios de una lista

lista=[1,2,3,4,"","curl","","arp",""," "]
sin_strings=[]

for i in lista:
	if(i!="" and i!=" "):
		sin_strings.append(i)

print(sin_strings)

