print("=========")
print("Conversor")
print("========= \n")

print("Menú de opciones: \n")
print("Presiona 1 para convertir de número a palabra.")
print("Presiona 1 para convertir de palabra a número. \n")

opcion = int(input("¿Cual es tu opción deseada?:"))

if opcion == 1:
    print("\n Conversor de número a palabra. \n")

    opcion_uno = int(input("¿Cual es el número que deseas convertir a palabra?: "))

    if opcion_uno == 1:
        print("El numero es 'UNO'")
    elif opcion_uno == 2:
        print("El numero es 'DOS'")
    elif opcion_uno == 3:
        print("El numero es 'TRES'")
    elif opcion_uno == 4:
        print("El numero es 'CUATRO'")
    elif opcion_uno == 5:
        print("El numero es 'CINCO'")
    else:
        print("El número seleccionado no está registrado.")

elif opcion ==2:
    print("\n Conversor de palabra a número. \n")

    opcion_dos = input("¿Cual es la palabra que desead convertir en número?: ")
    opcion_dos = opcion_dos.lower()

    if opcion_dos == "uno":
        print("El número es '1'")
    elif opcion_dos == "dos":
        print("El número es '2'")
    elif opcion_dos == "tres":
        print("El número es '3'")
    elif opcion_dos == "cuatro":
        print("El número es '4'")
    elif opcion_dos == "cinco":
        print("El número es '5'")
    else:
        print("El número seleccionado no está registrado.")

else:
    print("Opción no disponible.")

print("Fin.")
    


