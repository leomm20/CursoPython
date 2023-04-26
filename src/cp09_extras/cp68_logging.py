import logging
logging.debug('Texto debug')
logging.info('Texto info')
logging.warning('Texto warning')
logging.error('Texto error')
logging.critical('Texto critical')

"""Por defecto, los mensajes se mostrarán a partir de Warning, pero podés bajar a Info o 
Debug con setLevel, o bien, que sólo muestre Error o Critical.
"""

# Por ejemplo, si queremos que muestre todos los tipos de mensajes:
logging.root.setLevel(logging.DEBUG)

# Y si queremos que sólo muestre a partir de Error:
logging.root.setLevel(logging.ERROR)

# Y si en lugar de que aparezca en consola, querés que quede registrado en un archivo:
# filemode = ‘w’ limpiará el archivo
# filemode = ‘a’ agregará las líneas al final
logging.basicConfig(filename='ejemplo.log', encoding='utf-8', filemode='w', level=logging.INFO)
