"""Tenés que registrarte en https://platform.openai.com/docs/api-reference/introduction
Luego, abrir el menú (haciendo click en la imagen de tu perfil), clickear en View API Keys
En la página que se abrirá, clickear en “+ Create new secret key”
Va a aparecer un popup con la API_KEY generada"""

import sys
import openai


def consultar_openai(prompt, pedido_viejo='', context=''):
    try:
        r = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'user', 'content': pedido_viejo},
                {'role': 'assistant', 'content': context},
                {'role': 'user', 'content': prompt}
            ]
        )
        data = r["choices"][0]["message"]["content"]
    except Exception as err:
        data = str(err)
    return data


def consultar():
    global pedido_anterior
    global resp_anterior
    if 'cambio de tema' in pedido.lower():
        pedido_anterior = resp_anterior = ''
    respuesta = consultar_openai(pedido, pedido_anterior, resp_anterior)
    if respuesta.split() == '':
        msg = 'SIN RESPUESTA\n'
        print(msg)
    else:
        if 'that model is currently overloaded' not in respuesta.lower():
            resp_anterior = respuesta
        pedido_anterior = pedido
        print(f'Respuesta:\n{respuesta}\n**FIN**')


API_KEY = ''
openai.api_key = API_KEY

pedido_anterior = ''
resp_anterior = ''

while True:
    print()
    pedido = input('Ingresar pedido (exit para salir): ')
    if pedido.strip() == '':
        continue
    if pedido != 'exit':
        consultar()
    else:
        print('Hasta luego!')
        sys.exit()
