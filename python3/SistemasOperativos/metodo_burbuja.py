import random

mi_lista = random.sample(range(1000), 10)
print(mi_lista)

def ord_burbuja(arreglo):
    n = len(arreglo)

    for i in range(n-1):       # <-- bucle padre
        for j in range(n-1-i): # <-- bucle hijo
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

ord_burbuja(mi_lista)

print(mi_lista)
