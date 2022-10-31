import threading
import random

# VARIABLES GLOBALES
mi_lista = random.sample(range(1000), 500)
semaforos = [threading.Semaphore(1) for i in range(0,20)]
ordenado = False


# ORDENAMIENTO BURBUJA
def burbuja(arreglo):
    n = len(arreglo)
    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
    return arreglo

# 5 HILOS EN EJECUCION LOS CUALES VAN A COMPETIR PARA OBTENER UN RANGO LIBRE
def competir():
    global mi_lista
    j=0
    for semaforo in semaforos:
        if(semaforo._value == 1):
            mi_lista[j:j+25] = burbuja(mi_lista[j:j+25])
            semaforo.acquire()
            j+=25
        else:
            semaforo.release()
            continue

# CREAR 5 HILOS
def hilos():
    for k in range(5):
        threading.Thread(target=competir).start()

def guardar_datos(mi_lista):
    ruta = "./Desktop/ordenado.txt"
    f = open(ruta, 'a+')
    
    for i in mi_lista:
        f.write(str(i) + "\n")
    f.close()

#####################################################################
print(mi_lista)

while ordenado == False:
    hilos()
    n=0
    for i in range(1, len(mi_lista)):
        if mi_lista[i-1] > mi_lista[i]:
            temp = mi_lista[i-1]
            mi_lista[i-1] = mi_lista[i]
            mi_lista[i] = temp
            break
    
    if i == len(mi_lista)-1:
        ordenado = True
        guardar_datos(mi_lista)
        
print(mi_lista)
