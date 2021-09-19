import urllib.request
import json

def main():
	objetivo = "https://ipinfo.io/181.65.252.34/json"
	urlli = urllib.request.urlopen(objetivo)
	cargajson = json.loads(urlli.read())

	for dato in cargajson:
		print (dato + " : " + cargajson[dato])

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
