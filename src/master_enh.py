# ARCHIVO: mastermind5.py

# modulo que va a permitir elegir numeros aleatoriamente
import random

# el conjunto de simbolos validos en el codigo
digitos = ('0','1','2','3','4','5','6','7','8','9')

# "elegimos" el codigo
cant_digitos = 5
codigo = ''
for i in range(cant_digitos):
    candidato = random.choice(digitos)
    # vamos eligiendo digitos no repetidos
    while candidato in codigo:
        candidato = random.choice(digitos)
    codigo = codigo + candidato

# iniciamos interaccion con el usuario
print "Bienvenido/a al Mastermind!"
print "Tenes que adivinar un numero de %d cifras distintas" % cant_digitos
propuesta = raw_input("Que codigo propones?: ")

# procesamos las propuestas e indicamos aciertos y coincidencias
intentos = 1
while propuesta != codigo and propuesta != "Me doy":
    intentos = intentos + 1
    aciertos = 0
    coincidencias = 0

    # recorremos la propuesta y verificamos en el codigo
    for i in range(cant_digitos):
        if propuesta[i] == codigo[i]:
            aciertos = aciertos + 1
        elif propuesta[i] in codigo:
            coincidencias = coincidencias + 1
    print "Tu propuesta (%s) tiene %d aciertos y %d coincidencias." % \
        (propuesta, aciertos, coincidencias)
    # pedimos siguiente propuesta
    propuesta = raw_input("Propone otro codigo: ")

if propuesta == "Me doy":
    print "El codigo era: %s" % codigo
    print "Suerte la proxima vez!"
else:
    print "Felicitaciones! Adivinaste el codigo en %d intentos." % intentos
