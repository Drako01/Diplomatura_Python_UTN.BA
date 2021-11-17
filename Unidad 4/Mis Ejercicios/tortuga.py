import turtle

turtle.getscreen()
turtle.title("2 Estrellas")
turtle.shape("turtle")
turtle.shapesize(2, 2, 2)
turtle.color("blue", "green")
turtle.pensize(6)

turtle.begin_fill()
turtle.rt(45)
for i in range(8):
    turtle.fd(300)
    turtle.rt(135)
turtle.end_fill()


turtle.mainloop()
