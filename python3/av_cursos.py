import requests
import re

url = "http://aulavirtual.sistemas.unmsm.edu.pe/pregrado2017/login/index.php"

data = {
	"username":"USER",
	"password":"PASS",
	"rememberusername":"1"
}

s = requests.post(url, data=data)

if "Invalid login, please try again" in s.text:
	print("[!] No pudo iniciar sesion")

else:
	print("[*] Login success")
	out = re.findall('title="(.*?)" h', s.text)

	for item in out:
		print(item)

#Success
# python3 temp.py | grep -v "<" | grep -i "SOF"
