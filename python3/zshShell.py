#!/usr/bin/python
from sys import argv
from pynput.keyboard import Key, Controller
from time import sleep
keyboard = Controller()

try:
	version = argv[1]
except:
	version = ""
sleep(2)

keyboard.type("python"+version+" -c 'import pty; pty.spawn(\"/bin/bash\")'")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

sleep(0.5)
keyboard.press(Key.ctrl)
keyboard.press('z')
keyboard.release(Key.ctrl)
keyboard.release('z')

sleep(0.5)
keyboard.type("stty raw -echo;fg")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

sleep(1.0)
keyboard.type("xterm")
keyboard.press(Key.enter)
keyboard.release(Key.enter)

sleep(0.5)
keyboard.type("export TERM=xterm")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(0.5)

keyboard.type("stty rows 36 columns 135")
keyboard.press(Key.enter)
keyboard.release(Key.enter)
sleep(0.5)

