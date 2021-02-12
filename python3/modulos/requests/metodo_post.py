import requests

auth_data = {'username': 'eto.eto', 'password': 'hackerl4nd', 'rememberusername':'1'}
resp = requests.post('http://aulavirtual.sistemas.unmsm.edu.pe/pregrado2017/login/index.php', data=auth_data)

print(resp.status_code)
