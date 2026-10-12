empleados = ["Ana", "Luis", "Maria", "Carlos"]

print("Lista de empleados: ")

for empleado in empleados:
    print(empleado)

print("total de empleados: ", len(empleados))

nombre_buscado = input("Nombre del empleado a buscar: ")

if nombre_buscado in empleados:
    print("Empleado encontrado")
else:
    print("Empleado no encontrado")