import turtle

mijazz = turtle.Turtle()

strlados = input("¿Cuantos lados quieres? ")

lados = int(strlados)

for _ in range(0, 360, 15):
    for _ in range(0,lados):
        mijazz.forward(50)
        mijazz.left(360/lados)
    mijazz.left(15)
