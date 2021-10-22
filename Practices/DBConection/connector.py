import mysql.connector

mi_conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "7111"
)

if mi_conexion.is_connected:
    print("Conexión establecida correctamente")
else:
    print("No se ha podido establecer conexión")

mi_cursor = mi_conexion.cursor()

mi_cursor.execute("SHOW DATABASES")

for db in mi_cursor:
    print(db)

cursor_cerrado = mi_cursor.close()
if cursor_cerrado:
    print("Cursor cerrado con éxito")
else:
    print("El cursor no ha sido cerrado")

mi_conexion.close()
if mi_conexion.is_connected:
    print("Conexión sin cerrar, cuidado!")
else:
    print("Conexion cerrada con éxito")