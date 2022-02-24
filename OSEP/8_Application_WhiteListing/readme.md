## Alternate Data Stream
type test.txt > "c:\Temp\archivo.md:test.txt"
type test.txt > "c:\Temp\archivo.md:data.txt"

### Mostrar secuencia alternativa de datos
dir /r

### Visualizar ADS
more < "c:\Temp\archivo.md:test.txt"

----

## Modos de lenguaje PowerShell
- FullLanguage
- ConstrainedLanguage (introducido en PowerShell 3.0)
- RestrictedLanguage
- NoLanguage

[https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/](https://devblogs.microsoft.com/powershell/powershell-constrained-language-mode/)


#### Visualizar permisos de escritura
```accesschk64.exe "Users" c:/Windows -w```
