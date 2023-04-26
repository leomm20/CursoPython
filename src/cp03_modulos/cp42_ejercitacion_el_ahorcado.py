from random import choice


def elegir_palabra_secreta():
    lista = ["chancho", "camioneta", "cascarrabias", "felpudo", "vinoteca", "horripilante", "kilimanjaro"]
    return choice(lista)


def validar_dibujar_pantalla(pantalla, palabra, letra):
    acierto = False
    pantalla = list(pantalla)
    for i in range(len(palabra)):
        if palabra[i] == letra:
            pantalla[i] = letra
            acierto = True
    pantalla = "".join(pantalla).upper()
    print(pantalla)
    return acierto, pantalla


def pedir_letra(lista_no_acertadas, lista_acertadas):
    letras_aceptadas = "abcdefghijklmnñopqrstuvwxyz"
    letra1 = input("elegí una letra o arriesgá la palabra (escribí exit para salir): ").lower().strip()
    if letra1 == 'exit':
        return letra1
    while True:
        if len(letra1) > 1:
            if letra1 in lista_no_acertadas:
                letra1 = input("ya la habías dicho, te la perdono! "
                               "probá con otra (escribí exit para salir): ").lower()
            else:
                return letra1
        else:
            valida = []
            for letra in letras_aceptadas:
                valida.append(letra1 == letra)
            if True not in valida:
                letra1 = input("no es una letra válida! Te la perdono, "
                               "probá con otra (escribí exit para salir): ").lower()
            elif letra1 in lista_no_acertadas or letra1 in lista_acertadas:
                letra1 = input("ya la habías dicho, te la perdono! "
                               "probá con otra (escribí exit para salir): ").lower()
            else:
                return letra1


def volver_a_jugar():
    preg = input("\nVolvemos a jugar (s/n)?: ").lower()
    while preg != "n" and preg != "s":
        preg = input("S o N!!! Volvemos a jugar? (s/n): ").lower()
    if preg == "s":
        print("Bien! Vamos!\n")
        return True
    else:
        print("\n BAAAH!!! ABURRID@!!!\n")
        return False


preg = True
while preg:
    vidas = 6
    print(f"voy a elegir una palabra secreta que tendrás que adivinar en {vidas} intentos:")
    palabra = elegir_palabra_secreta()
    print(f"la palabra que elegí tiene {len(palabra)} letras:")
    pantalla = "-" * len(palabra)
    print(pantalla)
    letra = ""
    lista_no_acertadas = []
    lista_acertadas = []
    while True:
        intento = pedir_letra(lista_no_acertadas, lista_acertadas)
        intento = intento.lower()
        if intento == "exit":
            print("\n BAAAH!!! ABURRID@!!!\n")
            preg = False
            break
        if intento == palabra:
            print("\n" + palabra.upper(), end=" -> ")
            print("ME GANASTE!!! GGGRR!!")
            preg = volver_a_jugar()
            break
        acierto, pantalla = validar_dibujar_pantalla(pantalla, palabra, intento)
        if acierto:
            if pantalla.find("-") >= 0:
                print("descubriste una!")
                lista_acertadas.append(intento)
            else:
                print("\n" + palabra.upper(), end=" -> ")
                print("ME GANASTE!!! GGGRR!!\n")
                preg = volver_a_jugar()
                break
        else:
            vidas -= 1
            if vidas > 0:
                lista_no_acertadas.append(intento)
                print(f"fallaste! te restan {vidas} intentos")
            else:
                print("\nPERDISTE!! JAJAJA!", end=" ")
                print(f"la palabra secreta era {palabra.upper()}")
                preg = volver_a_jugar()
                break
