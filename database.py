import sqlite3


def crear_table():
    conexion = sqlite3.connect("empleados.db")

    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleados(
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL
        )
    """)

    conexion.commit()

    conexion.close()

def obtener_empleados():
    conexion = sqlite3.connect("empleados.db")

    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre FROM empleados")

    registro = cursor.fetchall()

    conexion.close()

    return registro





