from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

colormode(255)
leo.color(99, 204, 250)
leo.speed(10)

leo.penup()
leo.goto(-200, 0)
leo.pendown()

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

leo.end_fill()

bob: Turtle = Turtle()
bob.color(0, 0, 0)
bob.speed(20)

bob.penup()
bob.goto(-200, 0)
bob.pendown()

side_length: float = 300

i: int = 0
while (i < 3):
    bob.forward(side_length)
    bob.left(120)
    side_length = side_length * 0.97
    i = i + 1
    
done()