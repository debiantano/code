#!/usr/bin/python3
import os
import requests

url = 'http://intelligence.htb/documents/'

for i in range(2020,2022):
    for j in range(1,13):
        for k in range(1,31):
            date = f'{i}-{j:02}-{k:02}-upload.pdf'
            r = requests.get(url+date)
            print (r.text)
            if (r.status_code == 200):
                print (date)
                #text = r.text
                os.system('mkdir pdf')
                os.system(f'wget {url}{date} -O pdf/{date}')
