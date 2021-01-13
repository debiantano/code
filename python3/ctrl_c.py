#!/usr/bin/env python

import signal, sys, time

def signal_handler(signal, frame):
  print("Saliendo del bucle ...")
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while(True):
	time.sleep(1)
	print("Ejecucion del programa")
