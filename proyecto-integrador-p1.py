#Armamos nuestra lista de estudiantes (cada uno es un diccionario)

estudiantes = [
    {"nombre": "Erika", "apellido": "Gonzalez", "nota": 9},
    {"nombre": "Karen", "apellido": "Guardia", "nota": 8},
    {"nombre": "Agustina", "apellido": "Grille", "nota": 7.5},
    {"nombre": "Nicolas", "apellido": "Gonzalez", "nota": 8.5},
]

#Con este bucle el print queda prolijo. Ejemplo: Erika Gonzalez - Nota: 9
#for estudiante in estudiantes:
#   print(f"{estudiante['nombre']} {estudiante['apellido']} - Nota: {estudiante['nota']}")

#Usamos Bubble Sort para ordenar por nota
def bubble_sort_nota(estudiantes): #Definimos la función bubble_sort_nota y su parámetro: estudiantes
    n = len(estudiantes) #En la variable n guardamos la cantidad total de estudiantes en la lista, lo usamos para controlar los ciclos for de nuestro algoritmo.
    for i in range(n): #Este bucle for es externo: se repite n veces. Es parte del algoritmo de Bubble Sort y va "burbujando" el valor más alot hacia el final de la lista en cada pasada.
        for j in range(0, n - i - 1): #Este bucle interno recorre desde el principio de la lista hasta una posición antes del final. El -i hace que cada pasada se reduzca el rango, porque los últimos elementos ya están ordenados. El -1 evita pasarse de índice (para poder hacer j + 1 sin error).
            if estudiantes[j]["nota"] < estudiantes[j + 1]["nota"]: #Este if compara la nota del estudiante en la posición j con la del siguiente (j + 1). Si la nota de j es menor, los intercambia. Esto significa que los mayores van "subiendo" primero: es un orden de mayor a menor. El signo > Ordena de menor a mayor y el signo < Ordena de mayor a menor
                estudiantes[j], estudiantes[j + 1] = estudiantes[j + 1], estudiantes[j] #Si la condición anterior se cumple, intercambia las posiciones de los dos estudiantes en la lista.

#Usamos Bubble Sort para también ordenar por apellido
def bubble_sort_apellido(estudiantes):
    n = len(estudiantes)
    for i in range(n):
        for j in range(0, n - i - 1):
            if estudiantes[j]["apellido"] > estudiantes[j + 1]["apellido"]:
                estudiantes[j], estudiantes[j + 1] = estudiantes[j + 1], estudiantes[j]

#Y finalmente para ordenamiento, usamos Bubble Sort para ordenar por nombre también:
def bubble_sort_nombre(estudiantes):
    n = len(estudiantes)
    for i in range(n):
        for j in range(0, n - i - 1):
            if estudiantes[j]["nombre"] > estudiantes[j + 1]["nombre"]:
                estudiantes[j], estudiantes[j + 1] = estudiantes[j + 1], estudiantes[j]

#Printeamos para ver cómo están ordenados por nota de mayor a menor:
print("\nOrdenados por nota:")
bubble_sort_nota(estudiantes)
for estudiante in estudiantes:
    print(f"{estudiante['nombre']} {estudiante['apellido']} - Nota: {estudiante['nota']}")

#Printeamos para ver cómo están ordenados por apellido en orden alfabético.
print("\nOrdenados por apellido:")
bubble_sort_apellido(estudiantes)
for estudiante in estudiantes:
    print(f"{estudiante['apellido']} {estudiante['nombre']} - Nota: {estudiante['nota']}")

#Printeamos el orden por nombre en orden alfabético.
print("\nOrdenados por nombre:")
bubble_sort_nombre(estudiantes)
for estudiante in estudiantes:
    print(f"{estudiante['nombre']} {estudiante['apellido']} - Nota: {estudiante['nota']}")


#Búsqueda binaria por nombre (requiere la lista ordenada por nombre)
