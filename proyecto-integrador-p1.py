#Armamos nuestra lista de estudiantes (cada uno es un diccionario)

estudiantes = [
    {"nombre": "Erika", "apellido": "Gonzalez", "nota": 9},
    {"nombre": "Karen", "apellido": "Guardia", "nota": 8},
    {"nombre": "Agustina", "apellido": "Grille", "nota": 7.5},
    {"nombre": "Nicolas", "apellido": "Gonzalez", "nota": 8.5},
]


#for estudiante in estudiantes:
#   print(f"{estudiante['nombre']} {estudiante['apellido']} - Nota: {estudiante['nota']}")

#Usamos Bubble Sort para ordenar por nota
def bubble_sort_nota(estudiantes):
    n = len(estudiantes)
    for i in range(n):
        for j in range(0, n - i - 1):
            if estudiantes[j]["nota"] < estudiantes[j + 1]["nota"]: # > Ordena de menor a mayor < Ordena de mayor a menor
                estudiantes[j], estudiantes[j + 1] = estudiantes[j + 1], estudiantes[j]

#Printeamos para ver cómo estan ordenados por nota de mayor a menor:
print("\nOrdenados por nota:")
bubble_sort_nota(estudiantes)
for estudiante in estudiantes:
    print(f"{estudiante['nombre']} {estudiante['apellido']} - Nota: {estudiante['nota']}")