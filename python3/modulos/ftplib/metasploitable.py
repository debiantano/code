#!/usr/bin/python3

from ftplib import FTP
import os

os.system("touch exploit1 exploit2 exploit3")
malicious_files=["exploit1", "exploit2", "exploit3"]

def ftp_session():
    ftp=FTP()
    ftp.connect("192.168.0.105",21)
    ftp.login("msfadmin","msfadmin")

    for item in malicious_files:
        fp=open(item,"rb")
        ftp.storbinary("STOR %s" %os.path.basename(item),fp, 1024)
        fp.close()


if __name__=="__main__":
    ftp_session()
