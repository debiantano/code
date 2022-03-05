#!/usr/bin/python3

import requests

s= requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')

print(r.text)
print(r.headers)
print(r.status_code)
