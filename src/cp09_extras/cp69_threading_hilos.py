import time
from threading import Thread


def imprimir1(texto1, texto2, num1):
    print('HILO1', texto1, texto2, num1)
    for i in range(1, 21):
        print('-HILO1-')


def imprimir2(texto3, texto4, num2):
    print('HILO2', texto3, texto4, num2)
    for n in range(21, 41):
        print('-HILO2-')


def imprimir3(texto5, texto6, num3):
    print('HILO3', texto5, texto6, num3)
    for z in range(41, 251):
        print('-HILO3-')


def ejecutando(hilo: Thread):
    if hilo.is_alive():
        print(f'EL HILO {hilo.name} AÚN ESTÁ VIVO')
    else:
        print(f'EL HILO {hilo.name} YA FINALIZÓ')


h1 = Thread(target=imprimir1, args=['texto1', 'texto2', 3])
h2 = Thread(target=imprimir2, args=['texto3', 'texto4', 4])
h3 = Thread(target=imprimir3, args=['texto5', 'texto6', 5])

print('*'*50, '-MAIN- INICIO HILO 1:')
h1.start()

print('*'*50, '-MAIN- INICIO HILO 2:')
h2.start()
h2.join()

print('*'*50, '-MAIN- ESTO SE IMPRIME PORQUE HILO 2 YA FINALIZÓ\n')
print('TIP: al join se le puede agregar un timeout, en segundos\n')

print('*'*50, '-MAIN- INICIO HILO 3:')
h3.start()
time.sleep(0.00000455153)

ejecutando(h3)
time.sleep(0.5)

ejecutando(h3)
