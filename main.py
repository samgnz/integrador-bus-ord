from funciones import *

#Armamos nuestra lista de estudiantes (cada uno es un diccionario)
lista_estudiantes = [
    {"nombre": "Erika", "apellido": "Gonzalez", "nota": 7.3},
    {"nombre": "Nicolas", "apellido": "Grande", "nota": 6},
    {"nombre": "Agustina", "apellido": "Grille", "nota": 7.5},
    {"nombre": "Karen", "apellido": "Guardia", "nota": 8.2}
]

def main():
    while True:
        menu_principal()
        opcion = int(input("Ingrese la opcion a trabajar: "))

        if opcion == 1:
            print(lista_estudiantes)
        elif opcion == 2:
            agregar_estudiante(lista_estudiantes)
            print("\nLista actualizada:")
            print(lista_estudiantes)
        elif opcion == 3: #falta🔲
            eliminar_estudiante()
        elif opcion == 4:
            apellido = input("Ingrese el apellido a buscar: ")
            busqueda_binaria(lista_estudiantes, apellido)
        elif opcion == 5:
            nota = int(input("Ingrese la nota a buscar: "))
            busqueda_lineal(lista_estudiantes, nota)
        elif opcion == 6:
            print("Elija una de las opciones del menú.")
            print("1. Ordenar por nota (mayor a menor)")
            print("2. Ordenar por nombre (A-Z)")
            subopcion = int(input("Ingrese la opcion a trabajar: "))
            if subopcion == 1:
                print("Lista de estudiantes ordenado por notas (de mayor a menor)\n")
                bubble_sort(lista_estudiantes, "nota", descendente=True)
            elif subopcion == 2:
                bubble_sort(lista_estudiantes, "nombre")
            else:
                print("Ingrese una opcion válida")
        elif opcion == 7:
            print("Elija una de las opciones del menú.")
            print("1. Promedio total")
            print("2. Alumnos desaprobados")
            print("3. Alumnos aprobados")
            subopcion = int(input("Ingrese la opcion a trabajar: "))
            if subopcion == 1:
                print("La nota promedio es", promedio_total(lista_estudiantes))
            elif subopcion == 2:
                print("La lista de alumnos desaprobados son:")
                clasificacion_alumnos(lista_estudiantes, "desaprobados")
            elif subopcion == 3:
                print("La lista de alumnos aprobados son:")
                clasificacion_alumnos(lista_estudiantes, "aprobados")
            else:
                print("Ingrese una opcion válida")
        elif opcion == 8:
            print("Cerrando programa")
            break
        else:
            print("Ingrese una opcion válida")



#ejecucion programa principal
main()