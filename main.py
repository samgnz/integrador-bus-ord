# Llamamos a nuestra función bubble sort
from funciones import bubble_sort
import copy  # Para hacer copias independientes de la lista

#Armamos nuestra lista de estudiantes (cada uno es un diccionario)

estudiantes = [
    {"nombre": "Erika", "apellido": "Gonzalez", "nota": 9},
    {"nombre": "Karen", "apellido": "Guardia", "nota": 8},
    {"nombre": "Agustina", "apellido": "Grille", "nota": 7.5},
    {"nombre": "Nicolas", "apellido": "Gonzalez", "nota": 8.5},
]

#Hacemos las copias independientes de la lista para que los ordenamientos no se afecten entre ellos.
por_nota = copy.deepcopy(estudiantes)
por_nombre = copy.deepcopy(estudiantes)
por_apellido = copy.deepcopy(estudiantes)

#Usamos la función importada de bubble sort
#Ordenamos por nota de mayor a menor
bubble_sort(por_nota, "nota", descendente=True)

#Ordenamos por apellido de A a Z
bubble_sort(por_apellido, "apellido")

#Ordenamos por nombre de A a Z
bubble_sort(por_nombre, "nombre")

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
    