#!/usr/bin/python3
import subprocess, re

process=subprocess.run(['nmap', '192.168.0.1/24', '-sn', '--min-rate', '8000'], check=True, stdout=subprocess.PIPE, universal_newlines=True)
output=process.stdout

list=output.split()

#print(list)
for i in list:
	if re.findall("^192",i):
		print(i)

