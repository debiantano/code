#### Permisos de un archivo
```
Get-Acl -Path C:\temp\ | Format-List
Get-Acl -Path .\cred.txt | Format-List -Property Path, Owner, Group, Access 
```

#### Obtiene los procesos que se ejecutan en el equipo local
```
Get-Services
Get-Process winlogon  | Format-List
```

