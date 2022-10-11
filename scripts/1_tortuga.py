import turtle

# personalizacion de la ventana
window = turtle.Screen()
window.title("Pruebas con turtle")
window.bgcolor("#68a0ed")
window.setup(500, 500)
window.setworldcoordinates(0, 500, 500, 0)

# personalizacion de la pluma
kame = turtle.Turtle()
kame.shape("turtle")
kame.color("darkgreen")
kame.pensize(2)
kame.speed(10)

# instrucciones de la pluma

for i in range(0, 6):
    kame.penup()
    kame.goto(i*50, i*25)
    kame.pendown()
    kame.circle(i*25)


turtle.mainloop()
