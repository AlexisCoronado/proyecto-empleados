import sqlite3

def crear_tabla():
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

def insertar_empleado(nombre):
    conexion = sqlite3.connect("empleados.db")

    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO empleados (nombre) VALUES (?)",
        (nombre,)           
    )

    conexion.commit()

    conexion.close()

def seleccionar_empleado(nombre):
    conexion = sqlite3.connect("empleados.db")

    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id, nombre FROM empleados WHERE LOWER(nombre) = LOWER(?)",
        (nombre,)
    )
    registro = cursor.fetchone()

    conexion.close()

    return registro

def borrar_empleados(identificador):

    conexion = sqlite3.connect("empleados.db")

    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM empleados WHERE id = ?",
        (identificador,)
    )
        
    filas_eliminadas = cursor.rowcount

    conexion.commit()

    conexion.close()

    return filas_eliminadas

def actualizar_empleado(identificador, nuevo_nombre):

    conexion = sqlite3.connect("empleados.db")

    cursor = conexion.cursor()

    cursor.execute(
        "UPDATE empleados SET nombre = ? WHERE id = ?",
        (nuevo_nombre, identificador)
    )

    filas_cambiadas = cursor.rowcount

    conexion.commit()

    conexion.close()

    return filas_cambiadas
    
