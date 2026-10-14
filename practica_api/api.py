import requests

url = "https://jsonplaceholder.typicode.com/users"

respuesta = requests.get(url, timeout=10)

print(respuesta.status_code)