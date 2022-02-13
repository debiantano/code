#!/usr/bon/python3

import socket
import sys


def scanHost(ip, startPort, endPort):
    print('[*] Starting TCP port scan on host %s' % ip)
    tcp_scan(ip, startPort, endPort)


def tcp_scan(ip, startPort, endPort):
    for port in range(startPort, endPort + 1):
        try:
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            if not tcp.connect_ex((ip, port)):
                print('[+] %s : %d/TCP Open' % (ip, port))
                tcp.close()

        except Exception:
            pass


if __name__ == '__main__':
    socket.setdefaulttimeout(0.01)

    if len(sys.argv) < 4:
        print('Usage: ./portScanner.py <IP address> <start> <end>')
        print('Example: ./portscanner.py 192.168.1.10 1 65535\n')

    elif len(sys.argv) >= 4:
        network   = sys.argv[1]
        startPort = int(sys.argv[2])
        endPort   = int(sys.argv[3])

    if len(sys.argv) == 4:
        scanHost(network, startPort, endPort)
