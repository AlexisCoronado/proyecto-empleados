from database import obtener_empleados, insertar_empleado, seleccionar_empleado, borrar_empleados, actualizar_empleado, crear_tabla
options = ""

def pause():
    input("Presiona enter para continuar...")

def mostrar_empleados(empleados):
    for empleado in empleados:
        print("ID: ", empleado[0], "| Nombre: ", empleado[1])
    count = len(empleados)
    print("Total de empleados: ",count)

def agregar_empleados():
    nombre = input("Escribe el nombre del empleado nuevo: ").strip()

    if nombre:
        insertar_empleado(nombre)
        print(nombre ,"Se agrego correctamente")
    else:
        print("No se puede agregar un empleado sin nombre")

def buscar_empleado():
    busqueda = input("Escribe el nombre del empleado que deseas buscar: ").strip()
    if busqueda:
        registro = seleccionar_empleado(busqueda)
        if registro is None:
            print("No se encontro registro del empleado")
        else:
            print("Se encontro al empleado: ")
            print("ID:", registro[0])
            print("Nombre:", registro[1])
    else:
        print("No se puede buscar sin escribir un nombre")

def eliminar_empleado():
    eliminacion = input("Escribe el ID del empleado que deseas eliminaar: ").strip()
    if eliminacion:
        if eliminacion.isdigit():
            identificador = int(eliminacion)
            registro_eliminado = borrar_empleados(identificador)
            if registro_eliminado == 1:
                print("Se elimino correctamente al empleado con el ID: ", identificador)
            else:
                print("No existe el empleado que se busco eliminar o el ID es incorrecto")
        else:
            print("No se puede eliminar un ID que es texto")
    else:
        print("No se puede eliminar un empleado sin escribir un ID")

def modificar_empleado():
    id_empleado = input("Ingresa el ID del empleado que deseas modificar: ").strip()
    if id_empleado:
        if id_empleado.isdigit():
            identificador = int(id_empleado)
            if identificador > 0:
                nuevo_nombre = input("Introduce el nuevo nombre del empleado: ").strip()
                if nuevo_nombre:
                    registro = actualizar_empleado(identificador, nuevo_nombre)
                    if registro == 0:
                        print("El ID del empleado que se trato de actualiza no existe")
                    else:
                        print("El empleado se ha actualizado correctamente")   
                else:
                    print("No se puede asignar un nombre vacio")
            else:
                print("No existe ID igual o menor a cero '0'")
        else:
            print("El ID debe de ser un numero entero")    
    else:
        print("No se puede modificar un empleado sin escribir su ID")

while True:
    print("=== Sistema De Empleados===")
    print("1. Mostrar empleados")
    print("2. Agregar empleado")
    print("3. Buscar empleado")
    print("4. Eliminar empleado")
    print("5. Actualizar empleado")
    print("6. Salir del programa")

    crear_tabla()

    options = input("Elige una opcion: ")
    if options == "1":
        empleados = obtener_empleados()
        print("=== Elegiste Mostrar empleado ===")
        mostrar_empleados(empleados)
    elif options == "2":
        print("Elegiste Agregar empleado")
        agregar_empleados()
    elif options == "3":
        empleados = obtener_empleados()
        print("Elegiste Buscar empleado")
        buscar_empleado()
    elif options == "4":
        print("Elegiste Eleminar empleado")
        eliminar_empleado()
    elif options == "5":
        print("Elegiste Actualizar empleado")
        modificar_empleado()
    elif options == "6":
        print("Vuelve pronto")
        break
    else:
        print("Esa opcion no existe, trata con una del menu") 
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
        
            
    lower_empleados = []
    for empleado in empleados:
        lower_empleados.append(empleado.lower())

    '''