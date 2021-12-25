#!/usr/bin/python3

import requests, re
from bs4 import BeautifulSoup

req = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
soup = BeautifulSoup(req.text, "lxml")

print(soup.h1)
print(soup.h1.string)
print(soup.h1["class"])
print(soup.h1["id"])
print(soup.h1.attrs)
