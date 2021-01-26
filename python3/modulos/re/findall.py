import re

lista_nombre=['Ana Gomez',
				'Maria Martin',
				'Sandra Lopez',
				'Santiago Martin',
				'Sandra Fernandez']

for elemento in lista_nombre:
	if re.findall('^Sandra',elemento):
		print(elemento)
print

for elemento in lista_nombre:
	if re .findall('Martin$',elemento):
		print (elemento)

'''
^  ->  comienzo de un string
$  ->  terminen con esa palabra
'''
