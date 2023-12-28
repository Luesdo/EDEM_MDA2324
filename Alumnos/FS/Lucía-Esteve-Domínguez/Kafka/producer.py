from confluent_kafka import Producer
from datos import Cotizacion
import json
import time

registros_cotizacion = [Cotizacion() for _ in range(50)]

registros_cotizacion.sort(key=lambda x: x.fecha)

producer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}
producer = Producer(producer_conf)

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# Enviar los registros
for cotizacion_instance in registros_cotizacion:
    cotizacion_json = cotizacion_instance.to_json()
    producer.produce('prueba1', cotizacion_json.encode('utf-8'), callback=delivery_report)
    producer.poll(0)
    time.sleep(1)  # Espera 2 segundo antes de enviar el siguiente registro

producer.flush()