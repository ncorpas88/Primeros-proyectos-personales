print("Sistema para calcular el promedio de un alumno.")

nombre = input("Para comenzar, ¿Cual es tu nombre?: ")

matematicas = int(input(nombre + " ¿Cual es tu calificación en matemáticas?: "))
quimica = int(input(nombre + " ¿Cual es tu calificación en química?: "))
biologia = int(input(nombre + " ¿Cual es tu calificación en biología?: "))

promedio = (matematicas + quimica + biologia) / 3
promedio = int(promedio)

if promedio >= 6:
    print('Felicidades ' + nombre + ' "aprobaste" con un promedio de: ', promedio)

print("Fin.")
