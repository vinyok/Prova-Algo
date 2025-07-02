from functools import *

sensor_enviado1 = {'id': 1 , 'leituras': [1, 2, 3, 51, 52]}
sensor_enviado2 = {'id': 2 , 'leituras': [1, 2, 3, 50, ]}

def controle_temperatura (sensor, sensor2):
    lista = []
    valores = sensor['leituras']
    count = 0
    resultado = list(filter(lambda x: x > 50, valores))
    lista.append(resultado)
    print(lista)
    print(resultado)
    for i in resultado:
        count += 1
    print(count)
    dic_final = {sensor['id']: count}
    print(dic_final)

controle_temperatura(sensor_enviado1, sensor_enviado2)    