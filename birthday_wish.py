import turtle

def draw_layer(color, radius, y_position):
    turtle.penup()
    turtle.goto(0, y_position)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    turtle.circle(radius)
    turtle.end_fill()

def draw_text(text, y_position, text_color):
    turtle.penup()
    turtle.goto(0, y_position)
    turtle.pendown()
    turtle.color(text_color)
    turtle.write(text, align="center", font=("Arial", 24, "bold"))

screen = turtle.Screen()
screen.bgcolor("pink")

draw_layer("maroon", 160, -270)
draw_text("HAPPY", -220, "silver")

draw_layer("green", 140, -160)
draw_text("BIRTHDAY", -100, "gold")

draw_layer("gold", 110, -40)
draw_text("TO YOU", 0, "green")

draw_layer("darkred", 5, 145)


turtle.penup()
turtle.goto(0, 150)
turtle.setheading(0)
turtle.pendown()
turtle.color("darkred")
for _ in range(8):
    turtle.forward(70)
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    turtle.backward(70)
    turtle.right(45)

draw_text("JOY", 245, "darkblue")

# turtle.penup()
# turtle.goto(0, 250)
# turtle.pendown()
# turtle.color("purple")
# turtle.write("Code_With_Ezra", align="center", font=("Arial", 8, "bold"))

turtle.hideturtle()
turtle.done()