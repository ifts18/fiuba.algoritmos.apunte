import csv, os

ARCHIVO = "agenda.csv"
CAMPOS = ("Nombre", "Apellido", "Telefono", "Cumpleaños")

def cargar_agenda(archivo):
    """Carga todos los datos del archivo en una lista y la devuelve."""
    agenda = []
    if not os.path.exists(archivo):
        return agenda
    with open(archivo) as f:
        datos_csv = csv.reader(f)
        encabezado = next(datos_csv)
        for item in datos_csv:
            agenda.append(item)
    return agenda

def guardar_agenda(agenda, archivo):
    """Guarda la agenda en el archivo."""
    with open(archivo, "w") as f:
        datos_csv = csv.writer(f)
        datos_csv.writerow(CAMPOS)
        datos_csv.writerows(agenda)

def leer_busqueda():
    """Solicita al usuario nombre y apellido y los devuelve."""
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    return nombre, apellido

def buscar(nombre, apellido, agenda):
    """Busca el primer item que coincida con nombre y con apellido."""
    for item in agenda:
        if nombre in item[0] and apellido in item[1]:
            return item
    return None

def menu_alta(nombre, apellido, agenda):
    """Pregunta si se desea ingresar un nombre y apellido y
       de ser así, pide los datos al usuario."""
    print("No se encuentra {} {} en la agenda.".format(nombre, apellido))
    confirmacion = input("¿Desea ingresarlo? (s/n): ")
    if confirmacion.lower() != "s":
        return
    telefono = input("Telefono: ")
    cumple = input("Cumpleaños: ")
    agenda.append([nombre, apellido, telefono, cumple])

def mostrar_item(item):
    """Muestra por pantalla un item en particular."""
    nombre, apellido, telefono, cumple = item
    print()
    print("{} {}".format(nombre, apellido))
    print("Telefono: {}".format(telefono))
    print("Cumpleaños: {}".format(cumple))
    print()

def menu_item():
    """Muestra por pantalla las opciones disponibles para un item
       existente."""
    o = input("b: borrar, m: modificar, ENTER para continuar (b/m): ")
    return o.lower()

def modificar(viejo, nuevo, agenda):
    """Reemplaza el item viejo con el nuevo, en la lista datos."""
    indice = agenda.index(viejo)
    agenda[indice] = nuevo

def menu_modificacion(item, agenda):
    """Solicita al usuario los datos para modificar una entrada."""
    nombre = input("Nuevo nombre: ")
    apellido = input("Nuevo apellido: ")
    telefono = input("Nuevo teléfono: ")
    cumple = input("Nuevo cumpleaños: ")
    modificar(item, [nombre, apellido, telefono, cumple], agenda)

def baja(item, agenda):
    """Elimina un item de la lista."""
    agenda.remove(item)

def confirmar_salida():
    """Solicita confirmación para salir"""
    confirmacion = input("¿Desea salir? (s/n): ")
    return confirmacion.lower() == "s"

def agenda():
    """Función principal de la agenda.
    Carga los datos del archivo, permite hacer búsquedas, modificar
    borrar, y al salir guarda. """
    agenda = cargar_agenda(ARCHIVO)
    while True:
        nombre, apellido = leer_busqueda()
        if nombre + apellido == "":
            if confirmar_salida():
                break
        item = buscar(nombre, apellido, agenda)
        if not item:
            menu_alta(nombre, apellido, agenda)
            continue
        mostrar_item(item)
        opcion = menu_item()
        if opcion == "m":
            menu_modificacion(item, agenda)
        elif opcion == "b":
            baja(item, agenda)
    guardar_agenda(agenda, ARCHIVO)

agenda()
