import requests 

session = requests.Session()
print(session.cookies.get_dict())

response = session.get("https://google.es")
print(session.cookies.get_dict())
