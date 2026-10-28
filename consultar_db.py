import sqlite3

conexion = sqlite3.connect("empleados.db")

cursor = conexion.cursor()

cursor.execute(
    "SELECT id, nombre FROM empleados"
)

registros = cursor.fetchall()

for registro in registros:
    print("ID: ", registro[0],"| Nombre: ", registro[1])


conexion.close()
