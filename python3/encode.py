#!/usr/bin/python3

import urllib.parse, sys, os

encode = urllib.parse.quote_plus(sys.argv[1])

print(encode)
os.system("echo '{}' | xclip -sel clip".format(encode))
