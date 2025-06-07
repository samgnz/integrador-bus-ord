def bubble_sort(estudiantes, clave, descendente=False):
    n = len(estudiantes)
    for i in range(n):
        for j in range(0, n - i - 1):
            a = estudiantes[j][clave]
            b = estudiantes[j + 1][clave]
            if (a < b and descendente) or (a > b and not descendente):
                estudiantes[j], estudiantes[j + 1] = estudiantes[j + 1], estudiantes[j]

#Búsqueda binaria por apellido (requiere la lista ordenada por apellido) -- usar busqueda binaria es la mas eficiente en listas ordenadas
def busqueda_binaria(lista_estudiantes, apellido):
    izquierda = 0
    derecha = len(lista_estudiantes) -1

    while izquierda <= derecha:
        medio = (izquierda + derecha)//2
        apellido_medio = lista_estudiantes[medio]["apellido"]

    if apellido_medio == apellido:
        return medio
    elif apellido_medio < apellido:
        izquierda = medio + 1
    else:
        derecha = medio - 1
    return -1