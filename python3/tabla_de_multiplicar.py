#!/usr/bin/pytthon3

m=int(input("Introduce otro numero: "))

while m<10:
    file=open("tabla.txt","a")

    for i in range(1,m+1):
        cadena=(str(i)+"*"+str(m)+"="+str(i*m))
        file.write(cadena + "\n")

    file.write("\n")
    break
    file.close()

else:
    print("[!] Error en introducir datos")
