import requests

url = "https://jsonplaceholder.typicode.com/users-inexistente"
try:
    respuesta = requests.get(url, timeout=10)

    respuesta.raise_for_status()
    '''Compruebaa si el servidor devolvio un error HTTP, como 404 0 500. si ocurre,
    genera una excepcion.'''

    usuarios = respuesta.json()
    '''Aqui se convierte el contenido de json a objetos de python, como listas o
    diccionarios'''

    for users in usuarios :
        print("Nombre: ",users["name"])
        print("Correo: ",users["email"])
        print()
except requests.exceptions.RequestException as error:
    print("Ocurrio un error en la consulta de la API")
    print(error)

