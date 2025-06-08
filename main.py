from funciones import *

#Armamos nuestra lista de estudiantes (cada uno es un diccionario) - ordenada alfabeticamente por apellido
lista_estudiantes = [
    {'nombre': 'Sofia', 'apellido': 'Alvarez', 'nota': 10},
    {'nombre': 'Erika', 'apellido': 'Gonzalez', 'nota': 9},
    {'nombre': 'Karen', 'apellido': 'Guardia', 'nota': 8},
    {'nombre': 'Agustina', 'apellido': 'Grille', 'nota': 7.5},
    {'nombre': 'Quimey', 'apellido': 'Herrera', 'nota': 5.5},
    {'nombre': 'Nicolas', 'apellido': 'Martinez', 'nota': 9.5},
    {'nombre': 'Tatiana', 'apellido': 'Suarez', 'nota': 2},
    {'nombre': 'Norma', 'apellido': 'Velazquez', 'nota': 8},
    {'nombre': 'Emilia', 'apellido': 'Zaragoza', 'nota': 1}
]

def main():
    while True:
        menu_principal()
        opcion = int(input("Ingrese la opcion a trabajar: "))

        if opcion == 1:
            print("\nLista de estudiantes")
            print("-"*20)
            listar_estudiantes(lista_estudiantes)            
        elif opcion == 2:
            agregar_estudiante(lista_estudiantes)
            print("\nLista actualizada:")
            print("-"*20)
            listar_estudiantes(lista_estudiantes)
        elif opcion == 3:
            eliminar_estudiante(lista_estudiantes)
            print("\nLista actualizada:")
            print("-"*20)
            listar_estudiantes(lista_estudiantes)
        elif opcion == 4:
            apellido = input("\nIngrese el apellido a buscar: ")
            print("-"*20)
            busqueda_binaria(lista_estudiantes, apellido)
        elif opcion == 5:
            nota = float(input("Ingrese la nota a buscar: "))
            busqueda_lineal(lista_estudiantes, nota)
        elif opcion == 6:
            print("\nElija una de las opciones del menú.")
            print("1. Ordenar por nota (mayor a menor)")
            print("2. Ordenar por nombre (A-Z)")
            subopcion = int(input("\nIngrese la opcion a trabajar: "))
            if subopcion == 1:
                print("Lista de estudiantes ordenado por notas (de mayor a menor)\n")
                print("-"*20)
                bubble_sort(lista_estudiantes, "nota", descendente=True)
            elif subopcion == 2:
                print("Lista de estudiantes ordenado por nombre (A-Z)\n")
                print("-"*20)
                bubble_sort(lista_estudiantes, "nombre")
            else:
                print("Ingrese una opcion válida")
        elif opcion == 7:
            print("\nElija una de las opciones del menú.")
            print("1. Promedio total")
            print("2. Alumnos desaprobados")
            print("3. Alumnos aprobados")
            subopcion = int(input("\nIngrese la opcion a trabajar: "))
            if subopcion == 1:
                print("-"*20)
                print(f"La nota promedio es {promedio_total(lista_estudiantes):.2f}")
            elif subopcion == 2:
                print("-"*20)
                print("La lista de alumnos desaprobados son:")
                clasificacion_alumnos(lista_estudiantes, "desaprobados")
            elif subopcion == 3:
                print("-"*20)
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