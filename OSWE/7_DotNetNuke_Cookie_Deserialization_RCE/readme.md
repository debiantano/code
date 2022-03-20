### Instalacion
- Codigo fuente: [https://github.com/dnnsoftware/Dnn.Platform/releases/tag/v9.1.0](https://github.com/dnnsoftware/Dnn.Platform/releases/tag/v9.1.0)
- Configuracion IIS [https://www.dnnsoftware.com/docs/designers/setup/set-up-dnn-folder.html](https://www.dnnsoftware.com/docs/designers/setup/set-up-dnn-folder.html)
- Dar permisos a la carpeta DNN9 para los usuario: `"Servicio de red" y "IIS AppPool\DNN9"`
- Iniciar servicio SQL Server
- Crear Base de Datos dnn9
- Nuevo usuario `dnn9user : dnn9user`
- `UserMapping` -> DNN9 - dn_owner - public

----

El enfoque principal del módulo estará dirigido al proceso de deserialización de `.Net`, y más específicamente en la clase XMLSerializer.

#### Serializacion
El concepto de serialización (y deserialización) existe en informática desde hace varios años. 
años. Su propósito es convertir una estructura de datos en un formato que pueda almacenarse o transmitirse a través de un enlace de red para consumo futuro.

#### Instancia de clase XmlSerializer
```
XmlSerializer serializer = new XmlSerializer(typeof(MyConsoleText));
```

----
### Debug
```
LINEA 11
[assembly: Debuggable(DebuggableAttribute.DebuggingModes.Default | DebuggableAttribute.DebuggingModes.DisableOptimizations | DebuggableAttribute.DebuggingModes.IgnoreSymbolStoreSequencePoints | DebuggableAttribute.DebuggingModes.EnableEditAndContinue)]
```
Hacer uso de  DNSPY 32 bits

Para el debug w3sp.exe usar dnspy64 como administrador (dnspy 5.0.7)
