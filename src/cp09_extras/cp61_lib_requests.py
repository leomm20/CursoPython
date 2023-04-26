import requests
import sys
response = requests.get(url='https://api.covidtracking.com/v1/us/current.json')
print(response)  # Response [200]
print(response.status_code)  # 200
'''
1xx Hold on
2xx OK
3xx Go away
4xx user fails
5xx server fails
'''
if response.status_code != 200:
    print('Bad response from API')
    sys.exit()

data = response.json()
print(data)
print('\n############\n')



print('# AGREGAR ARGUMENTOS')

"""
ATENCIÓN: Si tenés problemas con los certificados (errores de SSL, de 
certificados autofirmados, etc), vas a tener que practicar en tu computadora 
personal y no en la de la empresa.
"""

LAT = -34.61315
LNG = -58.37723
PARAMS = {
 'lat': LAT,
 'lng': LNG,
 'formatted': 0  # 24 hs
}
response = requests.get('https://api.sunrise-sunset.org/json', params=PARAMS)
# o
# response = requests.get(f'https://api.sunrise-sunset.org/json?lat={LAT}&lng={LNG}')
response.raise_for_status()
data = response.json()
print(data)
print(data['results']['sunrise'].split('T'))

