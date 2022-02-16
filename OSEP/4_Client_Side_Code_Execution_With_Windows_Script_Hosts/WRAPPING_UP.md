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


