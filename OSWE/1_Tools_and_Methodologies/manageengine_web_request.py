#!/usr/bin/python3
import requests
from colorama import Fore, Back, Style
import os

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

cmd = "stty size"
out = os.popen(cmd).read().strip()
out=out.split(" ")


def format_text(title,item):
	cr = '\r\n'
	section_break = cr + "*" * int(out[1]) + cr
	item = str(item)

	text = Style.BRIGHT + Fore.RED + title + Fore.RESET + section_break + item + section_break
	return text

r = requests.get('https://google.es/',verify=False)

print (format_text('r.status_code is: ',r.status_code))
print (format_text('r.headers is: ',r.headers))
print (format_text('r.cookies is: ',r.cookies))
print (format_text('r.text is: ',r.text))
