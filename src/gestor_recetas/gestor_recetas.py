import os
import shutil
from pathlib import Path


def clear():
    os.system('cls')
    print('\n'*1000)


def crear_categoria():
    global ruta, categoria
    categoria = input('Ingresá nombre de categoría: ').lower()
    while categoria == '':
        categoria = input('No ingresaste nada. Ingresá nombre de categoría: ').lower()
    if Path(ruta, categoria).exists():
        clear()
        print(f'\nLa categoría {categoria} ya existe!\n')
    else:
        os.makedirs(Path(ruta, categoria))
        clear()
        print(f'\nCategoría {categoria} creada!\n')


def elegir_categoria():
    global ruta
    categorias = list(ruta.iterdir())
    if len(categorias) < 1:
        print('Aún no existen categorías!\n')
        return False
    indices = []
    nombres = []
    while True:
        print("Seleccioná la opción:\n")
        for indice, nombre in enumerate(categorias):
            indices.append(str(indice))
            nombres.append(nombre)
            print(f'[{indice}] - {nombre.name}')
        print(f'[v] - Volver al menú principal\n')
        sel_categoria = input("Ingresá tu opción: ").lower()
        while sel_categoria not in indices and sel_categoria != 'v':
            sel_categoria = input('Opción incorrecta. Ingresá opción: ').lower()
        break
    if sel_categoria == 'v':
        clear()
        return False
    else:
        return nombres[int(sel_categoria)]


def crear_receta():
    global categoria, ruta
    categoria = elegir_categoria()
    if not categoria:
        return False
    clear()
    print(f'Estás en categoría {categoria.name}\n')

    titulo = input('Escribí un título para la receta: ').lower()
    while titulo == '':
        titulo = input('No escribiste nada. Escribí un título para la receta que acabás de crear: ').lower()
    titulo = titulo
    titulo_con_ext = titulo + '.txt'
    if os.path.exists(Path(ruta, categoria, titulo_con_ext)):
        clear()
        validar = input(f'La receta {titulo} ya existe. Sobreescribir? (s/n): ').lower()
        while validar not in ['s', 'n']:
            validar = input(f'No ingresaste nada. La receta {titulo} ya existe. Sobreescribir? (s/n): ').lower()
        if validar == 'n':
            clear()
            return False

    clear()
    texto = input('Ingresá la receta (escribí \\n para nueva línea): ').lower()
    while texto == '':
        texto = input('No escribiste nada. Ingresá la receta (escribí \\n para nueva línea): ').lower()
    texto = texto.replace('\\n', '\n')
    texto = texto.replace(' \n', '\n')
    texto = texto.replace('\n ', '\n')

    f = open(Path(categoria, titulo_con_ext), 'w')
    f.write(texto)
    f.close()
    clear()
    titulo = Path(categoria, titulo_con_ext).stem
    print(f'\nLa receta {titulo} fue creada!\n')


def elegir_receta():
    global categoria
    recetas = list(categoria.glob('*.txt'))
    if len(recetas) < 1:
        clear()
        print(f'Aún no hay recetas en la categoría {categoria.name}\n')
        return False
    indices = []
    nombres = []
    while True:
        print("Seleccioná la opción:\n")
        for indice, nombre in enumerate(recetas):
            indices.append(str(indice))
            nombres.append(nombre)
            print(f'[{indice}] - {nombre.stem}')
        print(f'[v] - Volver al menú principal\n')
        sel_receta = input("Ingresá tu opción: ").lower()
        while sel_receta not in indices and sel_receta != 'v':
            sel_receta = input('Opción incorrecta. Ingresá opción: ').lower()
        break
    if sel_receta == 'v':
        clear()
        return False
    else:
        return nombres[int(sel_receta)]


def leer_receta():
    receta = elegir_receta()
    if receta:
        clear()
        print(f'Detalle de receta {receta.stem}:\n')
        print(receta.read_text() + '\n')
        input('Presioná la tecla Enter para continuar...')
        clear()


def eliminar_receta():
    global ruta
    global categoria
    categoria = elegir_categoria()
    if not categoria:
        categoria = ''
        return False
    clear()
    receta = elegir_receta()
    if receta:
        clear()
        aceptar = input(f'Estás seguro de querer eliminar la receta {receta.name}? (s/n): ').lower()
        while aceptar not in ['s', 'n']:
            aceptar = input(f'No ingresaste nada. Estás seguro de querer eliminar la receta {receta.name}? (s/n): ').lower()
        if aceptar == 's':
            clear()
            os.remove(receta)
            print(f'La receta {receta.name} ha sido eliminada\n')
        else:
            clear()
            return False
    else:
        return False


def eliminar_categoria():
    global categoria
    categoria = elegir_categoria()
    if not categoria:
        categoria = ''
        return False
    clear()
    if categoria:
        cont_rec = len(list(Path(ruta, categoria).glob('**/*.txt')))
        if cont_rec > 0:
            aceptar = input(f'Estás seguro de querer eliminar la categoría {categoria.name}? CONTIENE {cont_rec} '
                            f'RECETAS!! (s/n): ').lower()
            while aceptar not in ['s', 'n']:
                aceptar = input(f'No ingresaste nada. Estás seguro de querer eliminar la categoría '
                                f'{categoria.name}? CONTIENE {cont_rec} RECETAS!! (s/n): ').lower()
        else:
            aceptar = input(f'Estás seguro de querer eliminar la categoría {categoria.name}? (s/n): ').lower()
            while aceptar not in ['s', 'n']:
                aceptar = input(f'No ingresaste nada. Estás seguro de querer eliminar la categoría '
                                f'{categoria.name}? (s/n): ').lower()
        if aceptar == 's':
            clear()
            shutil.rmtree(categoria)
            print(f'La categoría {categoria.name} ha sido eliminada\n')
        else:
            clear()
            return False
    else:
        return False


def realizar_backup():
    global ruta
    res = shutil.make_archive('backup', 'zip', ruta)
    print(f'Backup realizado! {res}\n')


usuario = input('Ingrese su nombre: ').lower().capitalize()
clear()
print("*" * 49)
print(" " * 15 + "Bienvenido " + f"{usuario}!")
print("*" * 49 + "\n")

ruta = Path(os.getcwd(), 'recetas')
if not ruta.exists():
    os.makedirs('recetas')
cant_recetas = 0
for e in ruta.glob('**/*.txt'):
    cant_recetas += 1

print(f'Existen {cant_recetas} recetas en el directorio {ruta}\n')
categoria = ''

# mostrar menu
while True:
    print("Seleccioná la opción:\n\n"
          "[1] - Leer receta\n"
          "[2] - Crear receta\n"
          "[3] - Crear categoría\n"
          "[4] - Eliminar receta\n"
          "[5] - Eliminar categoría\n"
          "[6] - Hacer Backup\n"
          "[7] - Finalizar programa\n")
    seleccion = input("Ingresá tu opción: ")
    match seleccion:
        case '1':
            clear()
            categoria = elegir_categoria()
            if categoria:
                clear()
                print(f'Has elegido la categoría {categoria.name}\n')
                leer_receta()
        case '2':
            clear()
            crear_receta()
        case '3':
            clear()
            crear_categoria()
        case '4':
            clear()
            eliminar_receta()
        case '5':
            clear()
            eliminar_categoria()
        case '6':
            clear()
            realizar_backup()
        case '7':
            clear()
            print(f'Gracias {usuario} por utilizar el Gestor de Recetas!\n')
            exit()
        case _:
            clear()
            print('Opción inválida\n')
