#!/usr/bin/python3

import sys, os
from urllib.parse import unquote

if len(sys.argv) != 2:
    print("Use: {} <str>".format(sys.argv[0]))
else:
    decode = unquote(sys.argv[1]);
    print(decode)
    os.system("echo '{}' | xclip -sel clip".format(decode))
