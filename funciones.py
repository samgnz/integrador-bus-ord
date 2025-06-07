def bubble_sort(estudiantes, clave, descendente=False):
    n = len(estudiantes)
    for i in range(n):
        for j in range(0, n - i - 1):
            a = estudiantes[j][clave]
            b = estudiantes[j + 1][clave]
            if (a < b and descendente) or (a > b and not descendente):
                estudiantes[j], estudiantes[j + 1] = estudiantes[j + 1], estudiantes[j]

