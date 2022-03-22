mport sqlite3

ry:
   mi_conexion = sqlite3.connect("database.db")
   cursor = mi_conexion.cursor()
   cursor.execute("CREATE TABLE persona (nombre VARCHAR(50), edad INTEGER)")

xcept Exception as e:
   print(e)
