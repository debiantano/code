#!/usr/bin/python3

import sys, os
from urllib.parse import unquote

decode = unquote(sys.argv[1]);

print(decode)
os.system("echo '{}' | xclip -sel clip".format(decode))
