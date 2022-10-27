import threading, time

def function(a,b,c):
    i=0
    while(i < b):
        time.sleep(c)
        i+=1
        print(f"[{a}] Hilo: cuenta numero {i}")

t1 = threading.Thread(target=function, args=(1,4,0.9))
t2 = threading.Thread(target=function, args=(2,6,1.3))
t3 = threading.Thread(target=function, args=(3,5,0.3))

t1.start()
t2.start()
t3.start()
