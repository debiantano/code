#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--url", "-u", required=True, dest="url", help="WebSocket URL")
parser.add_argument("--key", "-k", dest="key", help="openITCOCKPIT key")
parser.add_argument("--verbose", "-v", help="Print more data", action="store_true")
args=parser.parse_args()

url = args.url
print(type(url))
print(type(int(args.key)))
print(type(args.verbose))
