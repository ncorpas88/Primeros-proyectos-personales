import turtle

mijazz = turtle.Turtle()

respuesta = input("¿Quieres un triangúlo?")

if respuesta == "s" or respuesta =="S":
    for _ in range(0,3):
        mijazz.forward(50)
        mijazz.left(120)
else:
    for _ in range(0,4):
        mijazz.forward(50)
        mijazz.left(90)
    
