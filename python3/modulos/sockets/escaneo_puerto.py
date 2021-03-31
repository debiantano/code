import socket
import sys

if __name__=="__main__":
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if not tcp.connect_ex(("192.168.0.105", int(sys.argv[1]))):
        print("[+] Pueto Abierto")
    else:
        print("[-] Puerto Cerrado")

print(type(sys.argv[1]))
