import turtle

mijazz = turtle.Turtle()

strlados = input("¿Cuantos lados quieres? ")

lados = int(strlados)

if lados == 3:
    for _ in range(0,3):
        mijazz.forward(50)
        mijazz.left(120)
elif lados == 4:
    for _ in range(0,4):
        mijazz.forward(50)
        mijazz.left(90)    
else:
    print("No se dibujar más que cuadrados y triángulos")
    
