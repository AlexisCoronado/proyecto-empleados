
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
    nombre = input("Escribe el nombre del empleado nuevo: ").strip()
    if nombre:
        empleados.append(nombre)
        print(empleados)
        print("Se agrego correctamente")
    else:
        print("No se puede agregar un empleado sin nombre")

def buscar_empleado(empleados):
    lower_empleados = []
    for empleado in empleados:
        lower_empleados.append(empleado.lower())

    busqueda = input("Escribe el nombre del empleado que deseas buscar: ").strip().lower()
    if busqueda:
        if busqueda in lower_empleados:
            print("Se encontro el empleado: ", busqueda)
        else:
            print("No se encontro registro del empleado: ", busqueda)
    else:
        print("No se puede buscar sin escribir un nombre")

def eliminar_empleado(empleados):
    eliminacion = input("Escribe el nombre del empleado que deseas eliminaar: ").strip()
    if eliminacion:
        if eliminacion in empleados:
            empleados.remove(eliminacion)
            print("Se elimino correctamente al empleado")
        else:
            print("No existe el empleado que se busco eliminar")
    else:
        print("No se puede eliminar sin escribir un nombre")
        
while True:
    print("=== Sistema De Empleados===")
    print("1. Mostrar empleados")
    print("2. Agregar empleado")
    print("3. Buscar empleado")
    print("4. Eliminar empleado")
    print("5. Salir del programa")

    options = input("Elige una opcion: ")
    if options == "1":
        print("=== Elegiste Mostrar empleado ===")
        mostrar_empleados(empleados)
    elif options == "2":
        print("Elegiste Agregar empleado")
        agregar_empleados(empleados)
    elif options == "3":
        print("Elegiste Buscar empleado")
        buscar_empleado(empleados)
    elif options == "4":
        print("Elegiste Eleminar empleado")
        eliminar_empleado(empleados)
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