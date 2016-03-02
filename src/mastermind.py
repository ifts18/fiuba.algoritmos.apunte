import random

def mastermind():
    """Funcion principal del juego Mastermind"""
    print("Bienvenido/a al Mastermind!")
    print("Tienes que adivinar un numero de cuatro cifras distintas")

    codigo = elegir_codigo()
    intentos = 1
    propuesta = input("Que codigo propones?: ")

    while propuesta != codigo:
        intentos += 1
        aciertos, coincidencias = analizar_propuesta(propuesta, codigo)
        print("Tu propuesta ({}) tiene {} aciertos y {} coincidencias.".format(
            propuesta,
            aciertos,
            coincidencias
        ))
        propuesta = input("Propone otro codigo: ")

    print("Felicitaciones! Adivinaste el codigo en {} intentos.".format(intentos))

def elegir_codigo():
    """Devuelve un codigo de 4 digitos elegido al azar"""
    digitos = ('0','1','2','3','4','5','6','7','8','9')
    codigo = ''
    for i in range(4):
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
    for i in range(4):
        if propuesta[i] == codigo[i]:
            aciertos = aciertos + 1
        elif propuesta[i] in codigo:
            coincidencias = coincidencias + 1
    return aciertos, coincidencias

mastermind()
