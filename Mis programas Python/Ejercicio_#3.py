print("###########################################################################")
print("# Programa para determinar ¿Cúal es el número mas grande de tres números? #")
print("########################################################################### \n")

numero_uno = float(input("Introduce el primer número: "))
numero_dos = float(input("Introduce el segundo número: "))
numero_tres = float(input("Introduce el tercer número: "))

if numero_uno > numero_dos and numero_uno > numero_tres:
    print("El número ", numero_uno, " es el más gramde de los tres.")
elif numero_dos > numero_tres:
        print("El número ", numero_dos, " es el más grande de los tres.")
else:
    print("El número ", numero_tres, " es el más grande de los tres.")
print("Fin del programa.")
