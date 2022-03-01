### SMTP enum

**SMTP** Simple Mail Transport Protocol  
**VRFI** pide al servidor que verifique una dirección de correo electrónico

#### Iniciar servicio postfix
```
service postfix start
```

#### Enumeracion de usuarios
```
smtp-user-enum -M VRFY -U users.txt -t 192.168.10.12
ismtp -h 192.168.1.107:25 -e /root/Desktop/email.txt

```
