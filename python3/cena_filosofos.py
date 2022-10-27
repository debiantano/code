import threading
import time

def tomar_tenedores(tenedor1 : threading.Semaphore, tenedor2: threading.Semaphore, numero: int):
    try:
        tenedor1.acquire()
        tenedor2.acquire()  
    except:
        print("Existió un problema al momento de tomar tenedores")


def soltar_tenedores(tenedor1 : threading.Semaphore, tenedor2: threading.Semaphore, numero:int):
    try:
        print("El filósofo [" + str(numero) + "] terminó de comer. Ahora suelta los tenedores...")
        tenedor1.release()
        tenedor2.release()
    except:
        print("Existió un problema al momento de soltar tenedores")

#################################################################################################

def piensa(numero: int):
    print("El filósofo [" + str(numero) + "] está PENSANDO")
    time.sleep(1)

def come(numero: int, tenedores: list):
    print("El filósofo [" + str(numero) + "] se prepara para comer...")
    # Determinar los tenedores que le tocan
    tenedor1 = tenedores[numero-1]
    try:
        numtenedor2 = numero
        tenedor2 = tenedores[numero]
    except:
        numtenedor2 = 0
        tenedor2 = tenedores[0]
    # Tomar los tenedores
    tomar_tenedores(tenedor1, tenedor2, numero)
    print("El filosofo [" + str(numero) + "] toma los tenedores: " + str(numero-1) + " y " + str(numtenedor2))
    # Comer
    print("El filósofo [" + str(numero) + "] está COMIENDO ...")
    time.sleep(1)
    # Soltar los tenedores
    soltar_tenedores(tenedor1, tenedor2, numero)
    #input()

def filosofo(numero:int, tenedores:list):
    while(True):
        piensa(numero)
        come(numero, tenedores)
    
def main():
    tenedor1 = threading.Semaphore()
    tenedor2 = threading.Semaphore()
    tenedor3 = threading.Semaphore()
    tenedor4 = threading.Semaphore()
    tenedor5 = threading.Semaphore()
    tenedores = [tenedor1, tenedor2, tenedor3, tenedor4, tenedor5]
    philosopher_list = list()

    i = 1
    while i <= 5:
        philosopher = threading.Thread(target=filosofo, args=(i,tenedores))
        philosopher_list.append(philosopher)
        #time.sleep(1.5)
        i += 1

    for i in range(5):
        philosopher_list[i].start()
        
main()

'''
threads filosofos[i]
while True:
    pensar()
    tomar_tenedores(i, i+1)
    comer()
    dejar_tenedores(i+1)
'''
