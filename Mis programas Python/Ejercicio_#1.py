print("######################################")
print("'Sistema control de vacaciones Rappi' ")
print("###################################### \n")

nombre = input("Por favor introduce el nombre del empleado: ")
clave = int(input("Por favor introduce la clave de departamento: "))
años = int(input("Por favor introduce los años en la empresa: "))

if clave == 1:

    if años == 1 and años <= 2:
        print("El empleado ", nombre, "tiene derecho a 6 días de vacaciones. ")
    elif años >= 2 and años <= 6:
        print("El empleado ", nombre, "tiene derecho a 14 días de vacaciones. ")
    elif años >=7:
        print("El empleado ", nombre, "tiene derecho a 20 días de vacaciones. ")
    else:
        print("El empleado ", nombre, "aún notiene derecho a vacaciones. ")

elif clave == 2:
    if años == 1 and años <= 2:
        print("El empleado ", nombre, "tiene derecho a 7 días de vacaciones. ")
    elif años >= 2 and años <= 6:
        print("El empleado ", nombre, "tiene derecho a 15 días de vacaciones. ")
    elif años >=7:
        print("El empleado ", nombre, "tiene derecho a 22 días de vacaciones. ")
    else:
        print("El empleado ", nombre, "aún notiene derecho a vacaciones. ")


elif clave == 3:
    if años == 1 and años <= 2:
        print("El empleado ", nombre, "tiene derecho a 10 días de vacaciones. ")
    elif años >= 2 and años <= 6:
        print("El empleado ", nombre, "tiene derecho a 20 días de vacaciones. ")
    elif años >=7:
        print("El empleado ", nombre, "tiene derecho a 30 días de vacaciones. ")
    else:
        print("El empleado ", nombre, "aún notiene derecho a vacaciones. ")

else:
    print("La clave del departamento no existe, vuelve a intentarlo.")
