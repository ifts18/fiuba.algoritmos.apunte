def inscribir_alumnos():
    """Permite inscribir alumnos al curso"""

    print("Inscripcion en el curso de Algoritmos y Programación I")
    inscriptos = []
    while True:
        padron = int(input("Ingresa un padrón (<=0 para terminar): "))
        if padron <= 0:
            break
        inscriptos.append(padron)
    return inscriptos

inscriptos = inscribir_alumnos()
print("La lista de inscriptos es:", inscriptos)
