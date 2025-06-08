from funciones import *

#Armamos nuestra lista de estudiantes (cada uno es un diccionario)
lista_estudiantes = [
    {"nombre": "Erika", "apellido": "Gonzalez", "nota": 9},
    {"nombre": "Karen", "apellido": "Guardia", "nota": 8},
    {"nombre": "Agustina", "apellido": "Grille", "nota": 7.5},
    {"nombre": "Nicolas", "apellido": "Gonzalez", "nota": 8.5},
    {"nombre": "Agustin", "apellido": "Perez", "nota": 2},
    {"nombre": "Silvia", "apellido": "Sosa", "nota": 4},
    {"nombre": "Pablo", "apellido": "Alberti", "nota": 6.5},
    {"nombre": "Nicolas", "apellido": "Martinez", "nota": 9.5},
    {"nombre": "Matias", "apellido": "Caballero", "nota": 10},
    {"nombre": "Sofia", "apellido": "Alvarez", "nota": 10},
    {"nombre": "Karen", "apellido": "Ortellado", "nota": 9},
    {"nombre": "Alan", "apellido": "Lupa", "nota": 8},
    {"nombre": "Brenda", "apellido": "Fernandez", "nota": 7},
    {"nombre": "Agustina", "apellido": "Ortiz", "nota": 2},
    {"nombre": "Jacqueline", "apellido": "Perez", "nota": 1},
    {"nombre": "Jeronimo", "apellido": "Acosta", "nota": 3},
    {"nombre": "Martina", "apellido": "Sanchez", "nota": 5},
    {"nombre": "Leila", "apellido": "Rios", "nota": 7},
    {"nombre": "Milagros", "apellido": "Baez", "nota": 6},
    {"nombre": "Juan", "apellido": "Castro", "nota": 8.5},
    {"nombre": "Alicia", "apellido": "Comisso", "nota": 4},
    {"nombre": "Melanie", "apellido": "Alonso", "nota": 8},
    {"nombre": "Diana", "apellido": "Cano", "nota": 7.5},
    {"nombre": "Quimey", "apellido": "Herrera", "nota": 5.5},
    {"nombre": "Thomas", "apellido": "Aguero", "nota": 3.5},
    {"nombre": "Melina", "apellido": "Bustamante", "nota": 8},
    {"nombre": "Oriana", "apellido": "Santoro", "nota": 4.5},
    {"nombre": "Natalia", "apellido": "Holzer", "nota": 8.5},
    {"nombre": "Tatiana", "apellido": "Suarez", "nota": 2},
    {"nombre": "Emilia", "apellido": "Zaragoza", "nota": 1},
    {"nombre": "Sol", "apellido": "Gutierrez", "nota": 5.5},
    {"nombre": "Norma", "apellido": "Velazquez", "nota": 8},
]

def main():
    while True:
        menu_principal()
        opcion = int(input("Ingrese la opcion a trabajar: "))

        if opcion == 1:
            bubble_sort(lista_estudiantes, "apellido")
        elif opcion == 2:
            proceso_agregar(lista_estudiantes)
        elif opcion == 3: 
            eliminar_estudiante(lista_estudiantes)
        elif opcion == 4:
            apellido = input("Ingrese el apellido a buscar: ")
            busqueda_binaria(lista_estudiantes, apellido)
        elif opcion == 5:
            nota = float(input("Ingrese la nota a buscar: "))
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
                print(f"La nota promedio es {promedio_total(lista_estudiantes):.2f}")
            elif subopcion == 2:
                print("La lista de alumnos desaprobados son:")
                clasificacion_alumnos(lista_estudiantes, "desaprobados")
            elif subopcion == 3:
                print("La lista de alumnos aprobados son:")
                clasificacion_alumnos(lista_estudiantes, "aprobados")
            else:
                print("Ingrese una opcion válida")
        elif opcion == 8:
            print("Cerrando programha")
            break
        else:
            print("Ingrese una opcion válida")



#ejecucion programa principal
main()