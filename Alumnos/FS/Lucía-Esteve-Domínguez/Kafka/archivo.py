#Caso de uso: Una aplicación que genere mensajes automáticos con información de tus acciones en función del mercado en el que te encuentras

#Importar librerias python
import random
import pandas as pd
from datetime import datetime, timedelta

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
            # Formatear la fecha directamente
        fecha_hora_aleatoria = fecha_aleatoria.strftime('%d/%m/%Y %H:%M:%S')
        return fecha_hora_aleatoria
       

    def __init__(self): 
        self.empresa = random.choice (list(self.lista_empresas.keys()))
        self.indice = self.lista_empresas[self.empresa]
        self.bolsa = self.lista_bolsas[self.indice]
        self.precio = random.uniform(0,100)
        self.fecha = self.generar_fecha_aleatoria()

#GENERACIÓN DATA SET Y ALMACENAMIENTO EN DF:
registros = [Cotizacion() for _ in range(1000)]

data = {
'empresa': [registro.empresa for registro in registros],
'indice': [registro.indice for registro in registros],
'bolsa': [registro.bolsa for registro in registros],
'precio': [registro.precio for registro in registros],
'Fecha': [registro.fecha for registro in registros],
}

df_cotizacion = pd.DataFrame(data)

#ORGANIZAMOS EL DATA SET POR FECHA (DE MÁS ANTIGUO A MÁS RECIENTE)
df_cotizacion['Fecha'] = pd.to_datetime(df_cotizacion['Fecha'])
df_cotizacion['Fecha'] = df_cotizacion['Fecha'].dt.strftime('%d/%m/%Y%H:%M:')
df_cotizacion = df_cotizacion.sort_values(by='Fecha')
df_cotizacion = df_cotizacion.reset_index(drop=True)

# Visualizar el DataFrame
print(df_cotizacion.head(100))
