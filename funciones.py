#Menú que se va a mostrar por consola
def menu_principal():
    print("\n¡Bienvenido/a a nuestro Sistema de Notas de la Universidad Tecnológica Nacional - Materia Programación 1!")
    print("Elija una de las opciones del menú.")
    print("1. Ver lista de estudiantes (ordenada alfabéticamente por apellido)")
    print("2. Agregar estudiante")
    print("3. Eliminar estudiante")
    print("4. Buscar un estudiante por apellido")
    print("5. Buscar nota")
    print("6. Ordenar lista")
    print("7. Mostrar estadísticas:")
    print("    1. Promedio total")
    print("    2. Alumnos desaprobados")
    print("    3. Alumnos aprobados")
    print("8. Salir")


#Función para agregar estudiante
def agregar_estudiante(lista_estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    nota = float(input("Ingrese la nota: "))
    estudiante = {f"nombre: {nombre} /n Apellido {apellido} /n Nota {nota}"}
    lista_estudiantes.append(estudiante)
# falta agregar el algoritmo insert sort


#Funcion para eliminar estudiante
def eliminar_estudiante():
    #algoritmo insert sort
    return 1

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

#Funcion para busqueda lineal - puede ser por nota o por nombre
def busqueda_lineal():
    #algoritmo busqueda lineal
    return 2

#Funcion para ordenar por burbuja - puede ser nota o nombre - por apellido la lista ya esta ordenada por defecto
def bubble_sort(lista_estudiantes, clave, descendente=False):
    n = len(lista_estudiantes)
    for i in range(n):
        for j in range(0, n - i - 1):
            a = lista_estudiantes[j][clave]
            b = lista_estudiantes[j + 1][clave]
            if (a < b and descendente) or (a > b and not descendente):
                lista_estudiantes[j], lista_estudiantes[j + 1] = lista_estudiantes[j + 1], lista_estudiantes[j]
    for estudiante in lista_estudiantes:
        print(f"{estudiante['nombre']}: {estudiante[clave]}")
