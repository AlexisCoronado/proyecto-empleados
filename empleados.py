
empleados = ["Ana", "Luis", "Maria", "Carlos"]
options = ""

def pause():
    input("Presiona enter para continuar...")

def mostrar_empleados(empleados):
    for empleado in empleados:
        print(empleado)
    count = len(empleados)
    print("Total de empleados: ",count)

def agregar_empleados(empleados):
    nombre = input("Escribe el nombre del empleado nuevo: ")
    if nombre.strip():
        empleados.append(nombre)
        print(empleados)
        print("Se agrego correctamente")
    else:
        print("ocurrio un problema")



while True:
    print("=== Sistema De Empleados===")
    print("1.  Mostrar empleados")
    print("2. Agregar empleado")
    print("3. Buscar empleado")
    print("4. Eliminar empleado")
    print("5. Salir del programa")

    options = input("Elige una opcion: ")
    if options == "1":
        print("=== Elegiste Mostrar empleado ===")
        mostrar_empleados(empleados)
        pause()
    elif options == "2":
        print("Elegiste Agregar empleado")
        agregar_empleados(empleados)
        pause()
    elif options == "3":
        print("Elegiste Buscar empleado")
        pause()
    elif options == "4":
        print("Elegiste Eleminar empleado")
        pause()
    elif options == "5":
        print("Vuelve pronto")
        break
    else:
        print("Upps, ocurrio un error trata otra vez")
        pause()
 

'''

print("Lista de empleados: ")

for empleado in empleados:
    print(empleado)

print("total de empleados: ", len(empleados))

nombre_buscado = input("Nombre del empleado a buscar: ")

if nombre_buscado in empleados:
    print("Empleado encontrado")
else:
    print("Empleado no encontrado")
    '''