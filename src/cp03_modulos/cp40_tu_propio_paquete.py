import paquete.subpaquete.saludo

paquete.subpaquete.saludo.saludar()

###########

from paquete.subpaquete import saludo

saludo.saludar()

###########

from paquete.subpaquete.saludo import saludar

saludar()

###########

"""
Incluso podrías compartir una librería en pypi.org, pero para eso ya tendrás que 
seguir ciertas pautas en el armado del módulo. 

Te dejo una página para que puedas profundizar en el tema:
https://www.freecodecamp.org/espanol/news/como-construir-tu-primer-paquete-depython
"""