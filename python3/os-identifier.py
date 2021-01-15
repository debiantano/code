#!/usr/bin/python3

import subprocess, re, sys

def return_ttl(address):
        proc=subprocess.Popen(["ping -c 1 %s" % address, ""], stdout=subprocess.PIPE, shell=True)
        (out,err)=proc.communicate()
        out=out.split()

        out=out[12].decode("utf-8")

        out=re.findall(r"\d{1,3}",out)
        return int(out[0])
#       return out[0]

#       print(out)
#       print(int(out[12].decode("utf-8")))

def return_ttl_os_name(ttl_number):
        if ttl_number>=0 and ttl_number<=64:
                return "Linux"
        elif ttl_number>=65 and ttl_number<=128:
                return "Windows"
        else:
                return "Unknown"

if (len(sys.argv)) !=2 :
        print("usage: os_identifier.py <ip>")
        sys.exit(1)

if __name__=='__main__':
        addr=sys.argv[1]
        ttl=return_ttl(addr)

        try:
                #print("\n%s -> %s" % (addr,return_ttl_os_name(int(ttl))))
                print("\n",addr, "->",return_ttl_os_name(ttl))
        except:
                print("hola")
