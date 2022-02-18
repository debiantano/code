#### Configurar carpeta de trabajo (sin comillas)
```!mona config -set workingfolder C:\Users\win7bits\Desktop\%p```

#### Generar badchars
```!mona bytearray -b "\x00"```   
```!mona bytearray -b "\x00\x07"```

#### Comparar haciendo referencia al bytearray que generó y la dirección a la que apunta ESP
```!mona compare -f C:\mona\appname\bytearray.bin -a <address>```

#### Encontrar el punto de salto
```!mona jmp -r esp -cpb \x07\x2e\xa0\x00"```   
```!mona jmp -r esp -cpb "\x00"```

#### Pattern create
```!mona pattern_create 1000```

#### Pattern offset
```!mona pattern_offset <direccion>```

#### Encuentre instrucciones en DLL específico
```
!mona find -s " " -m example.dll
!mona find -s "\xff\xe4" -m RM2MP3Converter.exe
```
