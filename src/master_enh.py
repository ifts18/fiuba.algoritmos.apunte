import random

CANT_DIGITOS = 5

def mastermind():
    """Funcion principal del juego Mastermind"""
    print("Bienvenido/a al Mastermind!")
    print("Tienes que adivinar un numero de {} cifras distintas".format(CANT_DIGITOS))

    codigo = elegir_codigo()
    intentos = 1
    propuesta = input("Que codigo propones?: ")
    ME_DOY = "Me doy"

    while propuesta != codigo and propuesta != ME_DOY:
        intentos += 1
        aciertos, coincidencias = analizar_propuesta(propuesta, codigo)
        print("Tu propuesta ({}) tiene {} aciertos y {} coincidencias.".format(
            propuesta,
            aciertos,
            coincidencias
        ))
        propuesta = input("Propone otro codigo: ")

    if propuesta == ME_DOY:
        print("Mala suerte! El código era: {}".format(codigo))
    else:
        print("Felicitaciones! Adivinaste el codigo en {} intentos.".format(intentos))

def elegir_codigo():
    """Devuelve un codigo de CANT_DIGITOS digitos elegido al azar"""
    digitos = ('0','1','2','3','4','5','6','7','8','9')
    codigo = ''
    for i in range(CANT_DIGITOS):
        candidato = random.choice(digitos)
        # Debemos asegurarnos de no repetir digitos
        while candidato in codigo:
            candidato = random.choice(digitos)
        codigo = codigo + candidato
    return codigo

def analizar_propuesta(propuesta, codigo):
    """Determina la cantidad de aciertos y coincidencias"""
    aciertos = 0
    coincidencias = 0
    for i in range(CANT_DIGITOS):
        if propuesta[i] == codigo[i]:
            aciertos = aciertos + 1
        elif propuesta[i] in codigo:
            coincidencias = coincidencias + 1
    return aciertos, coincidencias

mastermind()
