#!/usr/bin/python3

import urllib.parse, sys, os

if len(sys.argv) != 2:
    print("Use: {} <str>".format(sys.argv[0]))
else:
    encode = urllib.parse.quote_plus(sys.argv[1])
    print(encode)
    os.system("echo '{}' | xclip -sel clip".format(encode))


