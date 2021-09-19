#!/usr/bin/python3

from ftplib import FTP
ftp=FTP("ftp.us.debian.org")
ftp.login()

print(ftp.cwd("debian"))
ftp.retrlines("LIST")

with open("READNE", "wb") as fp:
    ftp.retrbinary('RETR README', fp.write)
ftp.quit()
