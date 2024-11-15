import turtle

def draw_heart():
    turtle.color('red')
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(180)
    turtle.circle(-90, 200)
    turtle.left(120)
    turtle.circle(-90, 200)
    turtle.forward(180)
    turtle.end_fill()

def draw_message():
    encrypted_message = [1044, 1072, 1088, 1080, 1085, 1072, 44, 32, 1103, 32, 1090, 1077, 1073, 1103, 32, 1083, 1102, 1073, 1083, 1102]
    message = ''.join(chr(i) for i in encrypted_message)
    turtle.penup()
    turtle.goto(-100, -50)
    turtle.color('black')
    turtle.write(message, font=("Arial", 16, "normal"))
    turtle.hideturtle()

turtle.speed(2)
draw_heart()
draw_message()
turtle.done()
