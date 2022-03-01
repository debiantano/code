#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 2:
    print "Usage: %s <username>" % sys.argv[0]
    sys.exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(('192.168.100.12',25))

try:
    f = open(sys.argv[1], "r")
    for line in f:
        s.send('VRFY ' + line.strip() + '\r\n')
        result = s.recv(1024)
        print result

except Exception as e:
    print str(e)
    sys.exit(0)
f.close()
