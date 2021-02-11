#!/usr/bin/python3

import socket
import sys

# Crea un socket TCP/IP
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlaza el socket con el puerto
port=4444
server_address=('localhost', port)
print("Starting server on port: " +str(port))

# Asociar el socket con la direccion del servidor
sock.bind(server_address)

# Escucha las conexiones entrantes
sock.listen(1)

while True:
	# Espera una conexion
	print("Esperando conexiones")
	connection, client_address=sock.accept()

	try:
		print('Conexion entrante de ' + str(client_address))

	# Procesa dato de entrada en un ciclo infinito
		while True:
			data=connection.recv(16)
			data=data[:1].decode("utf-8")

			if(len(data)>0):
				print('Dato_in: ' + str(data))

				if(data=='1'):
					print("Prender luz")
					connection.send(b'Hello!\n\r')

				if(data=='0'):
					print("Apagar luz")
					connection.send(b'Bye!\n\r')
				if(data=='q'):
					print('Finalizando conexiones con ' + str(client_address))
					break

	finally:
		# Cerrando el socket
		connection.close()
		sys.exit(0)

