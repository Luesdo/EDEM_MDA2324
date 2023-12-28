import requests
from requests.models import Response
URL : str = "https://api.chucknorris.io/jokes/random"

lista_chistes = []

#DEFINICIÓN DE FUNCIÓN
def chistes_Chuck_norris (numero_chistes):
    if numero_chistes > 5:
        print ("Valor no válido. Introduce un valor menor que 5")
    else:
        for numero in range (numero_chistes):
                respuesta : Response = requests.get(URL)
                datos = respuesta.json()
                frase_chuck: str = datos["value"]
                lista_chistes.append(frase_chuck)

    for chiste in lista_chistes:
        print (f'\n - {chiste}\n')
    print (f'Se han escrito {len(lista_chistes)} chistes')

#EJECUCIÓN DE FUNCIÓN
chistes_Chuck_norris(4)