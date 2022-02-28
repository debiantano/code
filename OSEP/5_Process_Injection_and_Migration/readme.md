## Process Injection

#### Process Injection
**OpenProcess** : obtenga un identificador del proceso remoto.  
**VirtualAllocEx** : cambia el estado de una región de memoria dentro de un proceso remoto.  
**WriteProcessMemory** : escribe datos en un proceso específico.  
**CreateRemoteThread** : inicia un hilo en un proceso remoto.  

----

**IntPtr hProcess = OpenProcess(0x001F0FFF, false, 3712)**  
**0x001F0FFF**: PROCESS_ALL_ACCESS   
**false**: Valor booleano que indica si queremos heredar los identificadores del otro proceso.  
**3712**: PID del proceso a acceder  

Una vez que tengamos un identificador del proceso, podemos asignar nuestro código de shell con VirtualAllocEx

**IntPtr addr = VirtualAllocEx(hProcess, IntPtr.Zero, 0x1000, 0x3000, 0x40)**  
**hProcess** es el controlador anterior que abrimos  
**IntPtr.Zero** podemos pasar nullptr a LPVOID porque queremos permitir que VirtualAllocEx determine dónde asignar espacio  
**0x1000** Tamaño del shellcode  
**0x3000** MEM_COMMIT|MEM_RESERVE. Donde MEM_RESERVE reservará el espacio requerido y MEM_COMMIT confirmará ese cambio en la memoria  
**0x40** constante de protección de la memoria (PAGE_EXECUTE_READWRITE),  permite leer, escribir y ejecutar en la región de páginas comprometida

**WriteProcessMemory(hProcess, addr, buf, buf.Length, out outSize)**  
**hProcess** identificador del proceso  
**addr** la dirección base que creamos con VirtualAllocEx  
**buf** el código de shell  
**bug.Length** el tamaño del shellcode  
**out outSize** parámetro de salida para la cantidad de bytes escritos  

**IntPtr hThread = CreateRemoteThread(hProcess, IntPtr.Zero, 0, addr, IntPtr.Zero, 0, IntPtr.Zero)**
**hProcess** identificador de ese proceso  
**IntPtr.Zero** se establece en nullptr, lo que esencialmente establece el descriptor de seguridad en el valor predeterminado y el identificador "no se puede heredar"  
**0** cantidad de shellcode para escribir  
**addr**  puntero a una función definida por la aplicación que se escribe en LPTHREAD_START_ROUTINE  
**IntPtr.Zero** se usa para acompañar la función anterior, ya que no estamos pasando datos, también podemos omitirlo y establecerlo en nullptr  
**0** establece la creación atribuida, 0 comenzará de inmediato  
**IntPtr.Zero** parámetro de salida opcional. Si no se necesita el ID del subproceso, se puede establecer en nullptr.   




