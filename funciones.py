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
    print("7. Mostrar estadísticas")
    print("8. Salir\n")

def listar_estudiantes(lista_estudiantes):
    for estudiante in lista_estudiantes:
        print(f"{estudiante['nombre']} {estudiante['apellido']} - Nota: {estudiante['nota']}")

#Función para agregar estudiante
def agregar_estudiante(lista_estudiantes):
    nuevo_estudiante = crear_estudiante()
    insercion_ordenada(lista_estudiantes, nuevo_estudiante)


def crear_estudiante():
    nombre = input("\nIngrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    nota = float(input("Ingrese la nota: "))
    estudiante = {"nombre": nombre, "apellido": apellido, "nota": nota}
    return estudiante

def insercion_ordenada(lista_estudiantes, nuevo_estudiante):
    apellido_nuevo_estudiante = nuevo_estudiante['apellido']

    for indice in range(len(lista_estudiantes)):
        apellido_estudiante_actual = lista_estudiantes[indice]['apellido']

        if apellido_estudiante_actual.lower() > apellido_nuevo_estudiante.lower():
            lista_estudiantes.insert(indice,nuevo_estudiante)
            break
        
        if indice == len(lista_estudiantes) - 1:
            lista_estudiantes.append(nuevo_estudiante)



#función eliminar_estudiante para eliminar estudiante
def eliminar_estudiante(lista_estudiantes):
    apellido = input("\nIngrese el apellido del estudiante a eliminar: ")
    izquierda = 0
    derecha = len(lista_estudiantes) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        apellido_medio = lista_estudiantes[medio]["apellido"]

        if apellido_medio == apellido:
            estudiante = lista_estudiantes[medio]
            confirmacion = input(f"¿Deseás eliminar a {estudiante['nombre']} {estudiante['apellido']} (s/n)? ").lower()
            if confirmacion == "s":
                lista_estudiantes.pop(medio) 
                print("Estudiante eliminado correctamente.")
            else:
                print("Operación cancelada.")
            return 
        elif apellido_medio < apellido:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    print(f"No se encontró ningún estudiante con el apellido '{apellido}'.")

#Búsqueda binaria por apellido (requiere la lista ordenada por apellido)
def busqueda_binaria(lista_estudiantes, apellido):
    izquierda = 0
    derecha = len(lista_estudiantes) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        apellido_medio = lista_estudiantes[medio]["apellido"]

        if apellido_medio == apellido:
            est = lista_estudiantes[medio]
            print(f"Estudiante encontrado: {est['nombre']} {est['apellido']} - Nota: {est['nota']}")
            return
        elif apellido_medio < apellido:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    print(f"El apellido '{apellido}' no fue encontrado")


#Funcion para busqueda lineal - puede ser por nota o por nombre
def busqueda_lineal(lista_estudiantes, nota):
    estudiantes = []

    for estudiante in lista_estudiantes:
        if estudiante["nota"] == nota:
            estudiantes.append({
                "nombre": estudiante["nombre"],
                "apellido": estudiante["apellido"],
                "nota": estudiante["nota"],
        })
            
    if estudiantes:
        for e in estudiantes:
            print(f'{e["nombre"]} {e["apellido"]} - Nota: {e["nota"]}')
    else:
        print("No se encontraron estudiantes con esa nota.")
    
    return estudiantes

#Funcion para ordenar por burbuja - puede ser nota o nombre - por apellido la lista ya esta ordenada por defecto
def bubble_sort(lista_estudiantes, clave, descendente=False):
    n = len(lista_estudiantes)
    for i in range(n):
        for j in range(0, n - i - 1):
            a = lista_estudiantes[j][clave]
            b = lista_estudiantes[j + 1][clave]
            if (a < b and descendente) or (a > b and not descendente):
                lista_estudiantes[j], lista_estudiantes[j + 1] = lista_estudiantes[j + 1], lista_estudiantes[j]
 # Mostrar la lista ordenada
    for estudiante in lista_estudiantes:
        print(f"{estudiante['nombre']} {estudiante['apellido']} - Nota: {estudiante['nota']}")

#Funcion promedio total
def promedio_total(lista_estudiantes):
    suma_notas = 0
    for estudiante in lista_estudiantes:
        suma_notas += estudiante["nota"]

    promedio = suma_notas / len(lista_estudiantes)

    return promedio

#Funcion clasificacion alumnos
def clasificacion_alumnos(lista_estudiantes, estado):
    resultados = []
    
    for estudiante in lista_estudiantes:
        if estado == "aprobados" and estudiante["nota"] >= 6:
            resultados.append(estudiante)
        elif estado == "desaprobados" and estudiante["nota"] < 6:
            resultados.append(estudiante)

    if resultados:
        for r in resultados:
            print(f'{r["nombre"]} {r["apellido"]} - Nota: {r["nota"]}')
    else:
        if estado == "aprobados":
            print("No hay alumnos aprobados.")
        else:
            print("No hay alumnos desaprobados.")
    
    return resultados