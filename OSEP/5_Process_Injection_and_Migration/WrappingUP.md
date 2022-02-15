**ZwCreateSection**: crea un objeto de sección que representa una sección de memoria que se puede compartir. Un proceso puede usar un objeto de sección para compartir partes de su espacio de direcciones de memoria (secciones de memoria) con otros procesos.

**ZwMapViewOfSection:**  asigna una vista de una sección al espacio de direcciones virtuales de un proceso en cuestión.

**ZwQueryInformationProcess:** recupera información sobre el proceso especificado.

**ZwUnmapViewOfSection:** desasigna una vista de una sección del espacio de direcciones virtuales de un proceso en cuestión.

**GetCurrentProcess:** recupera un pseudo identificador para el proceso actual.

**GetSystemInfo:** recupera información sobre el sistema actual.

**ReadProcessMemory:** lee datos de un área de memoria en un proceso específico.

**WriteProcessMemory:** escribe datos en un área de memoria en un proceso específico.

**ResumeThread:** disminuye el recuento de suspensión del subproceso. Cuando el recuento de suspensión se reduce a cero, se reanuda la ejecución del subproceso.

**CreateProcess:** crea un nuevo proceso y su subproceso principal. El nuevo proceso se ejecuta en el contexto de seguridad del proceso de llamada.
