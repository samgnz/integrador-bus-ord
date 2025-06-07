from funciones import bubble_sort, busqueda_binaria, menu_principal
import copy

#Armamos nuestra lista de estudiantes (cada uno es un diccionario)
lista_estudiantes = [
    {"nombre": "Erika", "apellido": "Gonzalez", "nota": 9},
    {"nombre": "Karen", "apellido": "Guardia", "nota": 8},
    {"nombre": "Agustina", "apellido": "Grille", "nota": 7.5},
    {"nombre": "Nicolas", "apellido": "Gonzalez", "nota": 8.5},
]

#Hacemos las copias independientes de la lista para que los ordenamientos no se afecten entre ellos.
por_nota = copy.deepcopy(lista_estudiantes)
por_nombre = copy.deepcopy(lista_estudiantes)
por_apellido = copy.deepcopy(lista_estudiantes)

#Usamos la función importada de bubble sort para ordenar por nota, apellido y nombre
bubble_sort(por_nota, "nota", descendente=True)
bubble_sort(por_apellido, "apellido")
bubble_sort(por_nombre, "nombre")

while True:
    menu_principal()
    opcion = int(input("\nSeleccione una opción: "))

    if opcion == 1:
        for estudiante in por_apellido:
            print(f"{estudiante['nombre']} {estudiante['apellido']} - Nota: {estudiante['nota']}")
    elif opcion == 2:
        
