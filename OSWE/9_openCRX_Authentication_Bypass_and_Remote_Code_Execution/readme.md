### openCRX 4.3.0 (JAVA)
OpenCRX es una aplicación de gestión de relaciones con los clientes (CRM) de código abierto de CRIXP Corp, y se utiliza para gestionar los flujos de ventas y marketing en una variedad de organizaciones, principalmente en los mercados europeos  
[https://github.com/opencrx/opencrx](https://github.com/opencrx/opencrx)

- Descarga [https://github.com/opencrx/opencrx/releases/tag/opencrx-v4.3.0](https://github.com/opencrx/opencrx/releases/tag/opencrx-v4.3.0)
- URL [http://localhost:8080/opencrx-core-CRX](http://localhost:8080/opencrx-core-CRX)
- Instalado en Windows 10
- JDK 1.8 
- Apache ant

----

#### JAR
es un tipo de archivo que permite ejecutar aplicaciones y herramientas escritas en el lenguaje Java. Los archivos JAR están comprimidos con el formato ZIP y cambiada su extensión a .jar

#### EAR
Un archivo EAR requiere un servidor de aplicaciones totalmente compatible con la plataforma Java, `Enterprise Edition (Java EE)` o `Jakarta Enterprise Edition (EE)` como `WebSphere` o `JBoss`, para ejecutarse.

#### WAR
Un archivo WAR solo requiere un servidor de aplicaciones compatible con `Java EE Web Profile` para ejecutarse

```
PASSWORDS DEFAULT
guest : guest
admin-Standard : admin-Standard
admin-Root : admin-Root
```

```
date +%s%3N && curl -s -i -X 'POST' --data-binary 'id=guest' 'http://192.168.100.2:8080/opencrx-core-CRX/RequestPasswordReset.jsp' && date +%s%3N

```
