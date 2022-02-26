#### Ver politica de ejecucion actual
```Get-ExecutionPolicy```

#### Mostrar la politica de ejecucion de cada ambito
```Get-ExecutionPolicy -List```

#### Cambiar GPO
```
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
Get-ExecutionPolicy -Scope CurrentUser
> Forma simplificada
powershell -ExecutionPolicy bypass
```


