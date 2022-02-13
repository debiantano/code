# dump() : volcado de datos al fichero binario externo
# load() : carga de los datos del fichero binario externo

import pickle
lista_nombres=["Mysql","Sqlite","MariaDB","MongoDB"]

fichero_binario=open("lista_nombres","wb")

pickle.dump(lista_nombres, fichero_binario)
fichero_binario.close()
