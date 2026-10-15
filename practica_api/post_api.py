import requests

url = "https://jsonplaceholder.typicode.com/users"

nuevo_usuario = {
    "name": "Carlos Martinez",
    "email": "carlos@example.com",
    "username": "carlosm"
}

try:
    respuesta = requests.post(
        url,
        json = nuevo_usuario,
        timeout=10
    )

    respuesta.raise_for_status()
    

    print("Codigo HTTP:", respuesta.status_code)
    print("Respuesta del servidor")
    print(respuesta.json())
    datos = respuesta.json()
    print(datos["name"])

except requests.exceptions.RequestException as error:
    print("Error al enviar los datos:")
    print(error)
