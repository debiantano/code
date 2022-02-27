#### Permisos de un archivo
```
Get-Acl -Path C:\temp\ | Format-List
Get-Acl -Path .\cred.txt | Format-List -Property Path, Owner, Group, Access 
accesschk.exe -uws "Everyone" "C:\Program Files"
find / -writable -type d 2>/dev/null
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

#### Firewall
```
netsh advfirewall show currentprofile
netsh advfirewall firewall show rule name=all
```

#### Tareas cron
```
schtasks /query /fo LIST /v
ls -lah /etc/cron*
cat /etc/crontab 
```

#### App instaladas
```
wmic product get name, version, vendor
wmic qfe get Caption, Description, HotFixID, InstalledOn
dpkg -l
```

#### Discos desmontados
```
mountvol
cat /etc/fstab
mout
/bin/lsblk
```

#### Enumeración de binarios que se elevan automáticamente
```
reg query HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\Installer
reg query HKEY_LOCAL_MACHINE\Software\Policies\Microsoft\Windows\Installer
find / -perm -u=s -type f 2>/dev/null
```

#### Deshabilitar todos los perfiles de firewall
```
netsh advfirewall set allprofiles state off 
```

#### Deshabilitando Windows Defender
```
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f > nul
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableRealtimeMonitoring /t REG_DWORD /d 1 /f > nul
```

