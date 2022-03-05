#### Configurando el entorno
```
student@atutor:~$ sudo nano /etc/mysql/my.cnf [mysqld] ... 
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

Después de pasar un tiempo haciéndolo, descubrimos un hallazgo potencialmente interesante. Miremos el código encontrado en ```/var/www/html/ATutor/mods/_standard/social/index_public.php```` 
```
14: $_user_location = 'public'; 15: 
16: define('AT_INCLUDE_PATH', '../../../include/'); 
17: require(AT_INCLUDE_PATH.'vitals.inc.php'); 
18: require_once(AT_SOCIAL_INCLUDE.'constants.inc.php'); 
19: require(AT_SOCIAL_INCLUDE.'friends.inc.php'); 
20: require(AT_SOCIAL_INCLUDE.'classes/PrivacyControl/PrivacyObject.class.php'); 
21: require(AT_SOCIAL_INCLUDE.'classes/PrivacyControl/PrivacyController.class.php'); 
```





