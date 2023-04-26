def suma(*args):
    resultado = 0.0
    try:
        for valor in args:
            resultado = resultado + float(valor)
    except:
        resultado = None
    return resultado


def resta(numero, *args):
    try:
        resultado = float(numero)
        for valor in args:
            resultado = resultado - float(valor)
    except:
        resultado = None
    return resultado
