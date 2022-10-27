import threading, pdb
sem1 = threading.Semaphore(0)
sem2 = threading.Semaphore(0)

def function1():
    print(1)
    sem1.release()
    sem2.acquire()
    print(3)
    sem1.release()

def function2():
    sem1.acquire()
    print(2)
    sem2.release()
    sem1.acquire()
    print(4)


threading.Thread(target=function1).start()
threading.Thread(target=function2).start()
