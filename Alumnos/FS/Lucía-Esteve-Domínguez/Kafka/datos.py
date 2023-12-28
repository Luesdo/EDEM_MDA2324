#Caso de uso: Una aplicación que genere mensajes automáticos con información de tus acciones en función del mercado en el que te encuentras

#Importar librerias python
import random
import pandas as pd
from datetime import datetime, timedelta
import json

#Definir los mercados, los indices y las empresas 
class Cotizacion:
    lista_empresas= {
    "Apple": "S&P 500",
    "Microsoft": "S&P 500",
    "Amazon": "S&P 500",
    "Facebook": "S&P 500",
    "Tesla": "S&P 500",
    "Berkshire Hathaway": "S&P 500",
    "JPMorgan Chase": "S&P 500",
    "Johnson & Johnson": "S&P 500",
    "Visa": "S&P 500",
    "Walmart": "S&P 500",
    "Gazprom": "MOEX",
    "Sberbank": "MOEX",
    "Lukoil": "MOEX",
    "Rosneft": "MOEX",
    "Novatek": "MOEX",
    "Nornickel": "MOEX",
    "Surgutneftegas": "MOEX",
    "Polyus": "MOEX",
    "Severstal": "MOEX",
    "Alrosa": "MOEX",
    "Banco Santander": "IBEX 35",
    "Inditex": "IBEX 35",
    "Iberdrola": "IBEX 35",
    "BBVA": "IBEX 35",
    "Telefónica": "IBEX 35",
    "Amadeus IT Group": "IBEX 35",
    "Ferrovial": "IBEX 35",
    "Repsol": "IBEX 35",
    "Acciona": "IBEX 35",
    "Mapfre": "IBEX 35",
    "Google (Alphabet)": "S&P 500",
    "Coca-Cola": "S&P 500",
    "Nike": "S&P 500",
    "Boeing": "S&P 500",
    "Goldman Sachs": "S&P 500",
    "Pfizer": "S&P 500",
    "Intel": "S&P 500",
    "Procter & Gamble": "S&P 500",
    "Chevron": "S&P 500",
    "McDonald's": "S&P 500",
    "Magnit": "MOEX",
    "Yandex": "MOEX",
    "MTS": "MOEX",
    "VimpelCom": "MOEX",
    "Tatneft": "MOEX",
    "X5 Retail Group": "MOEX",
    "Polymetal": "MOEX",
    "Magnitogorsk Iron and Steel Works": "MOEX",
    "Mail.ru Group": "MOEX",
    "PhosAgro": "MOEX",
    "CaixaBank": "IBEX 35",
    "Red Eléctrica": "IBEX 35",
    "Enagás": "IBEX 35",
    "Naturgy Energy": "IBEX 35",
    "Endesa": "IBEX 35",
    "Cellnex Telecom": "IBEX 35",
    "Aena": "IBEX 35",
    "Banco Sabadell": "IBEX 35",
    "Grifols": "IBEX 35",
    "Bankinter": "IBEX 35"
    }

    lista_bolsas = {
      "IBEX 35": "Bolsa Madrid",
       "MOEX": "Bolsa Moscu",
       "S&P 500": "Bolsa EEUU"
    }

#Definir tipo de dato hora y fecha
    @staticmethod
    def generar_fecha_aleatoria():
        start_date = datetime.today().replace(year=datetime.today().year - 1)
        end_date = datetime.today()
        tiempo_entre_fechas = end_date - start_date
        dias_aleatorios = random.randrange(tiempo_entre_fechas.days)
        fecha_aleatoria = start_date + timedelta(days=dias_aleatorios)
        return fecha_aleatoria
       

    def __init__(self): 
        self.empresa = random.choice (list(self.lista_empresas.keys()))
        self.indice = self.lista_empresas[self.empresa]
        self.bolsa = self.lista_bolsas[self.indice]
        self.precio = random.uniform(0,100)
        self.fecha = Cotizacion.generar_fecha_aleatoria()

    def to_json(self):
        data = self.__dict__.copy()
        data['fecha'] = self.fecha.strftime('%Y-%m-%d %H:%M:%S')
        return json.dumps(data)


