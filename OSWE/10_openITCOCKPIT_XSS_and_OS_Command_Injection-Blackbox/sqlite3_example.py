#!/usr/bin/python3
import sqlite3

conexion=sqlite3.connect("database.db")
try:
        conexion.execute("""
                CREATE TABLE articulos(
                        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                        descripcion TEXT,
                        precio REAL
                )
        """)
        print("[+] Tabla creada")
except Exception as e:
        print(str(e))

conexion.close()

####################################################################################################################################
####################################################################################################################################
#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect("database.db")
conn.execute("INSERT INTO articulos(descripcion,precio) values (?,?)", ("naranjas", 23.5))
conn.execute("INSERT INTO articulos(descripcion,precio) values (?,?)", ("peras", 13.2))
conn.execute("INSERT INTO articulos(descripcion,precio) values (?,?)", ("manzanas", 32.7))
conn.commit()
conn.close()

####################################################################################################################################
####################################################################################################################################
#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect("database.db")
codigo = int(input("Ingrese codigo: "))
cursor = conn.execute("SELECT descripcion,precio FROM articulos WHERE codigo=?", (codigo,))
fila = cursor.fetchone()

if (fila != None):
        print(fila)
else:
        print("Codigo incorrecto")
conn.close()

####################################################################################################################################
####################################################################################################################################
#!/usr/bin/python3
import sqlite3

conn=sqlite3.connect("database.db")
cursor=conn.execute("SELECT codigo,descripcion,precio FROM articulos")

for fila in cursor:
        print(fila)
conn.close()

####################################################################################################################################
####################################################################################################################################
#!/usr/bin/python3
import sqlite3

conn = sqlite3.connect("database.db")
precio = float(input("Ingrese precio: "))
cursor = conn.execute("SELECT descripcion,precio FROM articulos WHERE precio < ?", (precio,))
filas = cursor.fetchall()

if len(filas) > 0:
        for fila in filas:
                print(fila)
else:
        print("No existe articulos")
conn.close()
