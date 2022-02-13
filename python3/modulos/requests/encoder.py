#!/usr/bin/python3
#coding:utf-8

import requests
import re
import sys

url="https://www.urlencoder.org/"
decode=sys.argv[1]

def encoder():
    try:
        data_post={
            "input" : "%s" % decode,
            "charset" : "UTF-8",
            "separator" : "lf"
        }

        s=requests.post(url,data=data_post)
        string=re.findall(r"spellcheck=\"false\">(.*?)</textarea>", s.text)
        print(string[1])

    except Exception as e:
        print(str(e))

if __name__=="__main__":
    encoder()
