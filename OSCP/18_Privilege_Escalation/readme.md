#### Permisos de un archivo
```
Get-Acl -Path C:\temp\ | Format-List
Get-Acl -Path .\cred.txt | Format-List -Property Path, Owner, Group, Access 
```

#### Obtiene los procesos que se ejecutan en el equipo local
```
tasklist /SVC
Get-Services
Get-Process winlogon  | Format-List
```

#### Enumeracion
```
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"
cat /etc/issue
cat /etc/*-release
uname -a
```

#### Tablas de enrutamiento - red
```
route print
netstat -ano | finstr "TCP"

LINUX
/sbin/route
ip a
ss -anp
```






