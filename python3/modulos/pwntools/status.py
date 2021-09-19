from pwn import *
import time
import sys

p1=log.progress("payload")

i=0

for i in range(10):
	i+=1
	p1.status("limite {}".format(i))
	time.sleep(1)

	if(i==20):
		p1.failure("ha ocurrido un error")
		sys.exit(1)

p1.success("Successfully")
sys.exit(0)
