import requests, re

response=requests.get("https://www.y2mate.com/es9/convert-youtube")
state=re.findall(r'<img src="(.*?)"', response.text)[0]

print(state)
