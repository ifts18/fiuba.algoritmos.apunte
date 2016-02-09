import csv

def imprimir_notas_alumnos(alumnos, notas):
    """Procesa los archivos de alumnos y notas, y por cada
    alumno imprime todas las notas que le corresponden."""
    with open(notas) as f_notas, open(alumnos) as f_alumnos:
        notas_csv = csv.reader(f_notas)
        alumnos_csv = csv.reader(f_alumnos)

        # Saltea los encabezados
        next(notas_csv)
        next(alumnos_csv)

        # Empieza a leer
        alumno = next(alumnos_csv, None)
        nota = next(notas_csv, None)
        while alumno:
            padron, apellido, nombre, carrera = alumno
            print("{}, {} ({})".format(apellido, nombre, padron))
            if not nota or nota[0] != padron:
                print("\tNo se registran notas")
            while nota and nota[0] == padron:
                print("\t{}: {}".format(nota[1], nota[2]))
                nota = next(notas_csv, None)
            alumno = next(alumnos_csv, None)
