from funciones import *

#Armamos nuestra lista de estudiantes (cada uno es un diccionario)
lista_estudiantes = [
    {"nombre": "Erika", "apellido": "Gonzalez", "nota": 9},
    {"nombre": "Nicolas", "apellido": "Grande", "nota": 8.5},
    {"nombre": "Agustina", "apellido": "Grille", "nota": 7.5},
    {"nombre": "Karen", "apellido": "Guardia", "nota": 8}
]

def main():
    while True:
        menu_principal()
        opcion = int(input("Ingrese la opcion a trabajar: "))

        if opcion == 1:
            print(lista_estudiantes)
        elif opcion == 2:
            agregar_estudiante()
        elif opcion == 3:
            eliminar_estudiante()
        elif opcion == 4: #hecho ✔️
            apellido = input("Ingrese el apellido a buscar: ")
            busqueda_binaria(lista_estudiantes, apellido)
        elif opcion == 5:
            busqueda_lineal()
        elif opcion == 6: #hecho ✔️
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
                promedio_total()
            elif subopcion == 2:
                alumnos_desaprobados()
            elif subopcion == 3:
                alumnos_aprobados()
            else:
                print("Ingrese una opcion válida")
        elif opcion == 8:
            print("Cerrando programa")
            break
        else:
            print("Ingrese una opcion válida")



#ejecucion programa principal
main()