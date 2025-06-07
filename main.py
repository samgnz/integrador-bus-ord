# Llamamos a nuestra función bubble sort
from funciones import (
    bubble_sort,
    busqueda_binaria,
    menu_principal,
)

import copy  # Para hacer copias independientes de la lista

#Armamos nuestra lista de estudiantes (cada uno es un diccionario)
estudiantes = [
    {"nombre": "Erika", "apellido": "Gonzalez", "nota": 9},
    {"nombre": "Nicolas", "apellido": "Gonzalez", "nota": 8.5},
    {"nombre": "Agustina", "apellido": "Grille", "nota": 7.5},
    {"nombre": "Karen", "apellido": "Guardia", "nota": 8}
]

#Hacemos las copias independientes de la lista para que los ordenamientos no se afecten entre ellos.
por_nota = copy.deepcopy(estudiantes)
por_nombre = copy.deepcopy(estudiantes)
por_apellido = copy.deepcopy(estudiantes)

#Usamos la función importada de bubble sort para ordenar por nota, apellido y nombre
bubble_sort(por_nota, "nota", descendente=True)
bubble_sort(por_apellido, "apellido")
bubble_sort(por_nombre, "nombre")

#Buscamos por apellido
busqueda_binaria(estudiantes, "Gonzalez")

#Printeamos el resultado
#Mostramos el orden por nota (de mayor a menor)
print("Lista de estudiantes ordenado por notas (de mayor a menor)\n")
for estudiante in por_nota:
    print(f"{estudiante['nombre']} {estudiante['apellido']} - Nota: {estudiante['nota']}")

print("-------------")

#Mostramos el orden por apellido
print("Lista de estudiantes ordenado por apellido (A a Z)\n")
for estudiante in por_apellido:
    print(f"{estudiante['nombre']} {estudiante['apellido']} - Nota: {estudiante['nota']}")

print("------------")

#Mostramos el orden por apellido
print("Lista de estudiantes ordenado por nombre (A a Z)\n")
for estudiante in por_nombre:
    print(f"{estudiante['nombre']} {estudiante['apellido']} - Nota: {estudiante['nota']}")

print("------------")

#Mostramos la busqueda
print(busqueda_binaria)

    