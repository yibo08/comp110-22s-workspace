"""EX04 Turtle Scene Exercise -- Starry Night."""
from turtle import Turtle, done, colormode, screensize, tracer, update
from random import randint, uniform

_author_ = "730526118"

MAX_SPEED: int = 0


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)
    scene: Turtle = Turtle()
    screensize(800, 600, "black")
    star_generator(scene)
    draw_moon(scene, -500, 300)
    cloud_generator(scene)
    draw_milky(scene, 600, -400)
    update()
    done()


def draw_star(star: Turtle, x: float, y: float, width: float) -> None:
    """Draw a random color star."""
    star_color_r: int = randint(0, 255)
    star_color_g: int = randint(0, 255)
    star_color_b: int = randint(0, 255)
    colormode(255)
    star.color(star_color_r, star_color_g, star_color_b)
    star.fillcolor(star_color_r, star_color_g, star_color_b)
    star.speed(MAX_SPEED)
    star.hideturtle()
    star.penup()
    star.goto(x, y)
    star.pendown()
    i_star: int = 0
    star.begin_fill()
    while i_star < 5:
        star.forward(width)
        star.right(144)
        i_star += 1
    star.end_fill()


def draw_moon(moon: Turtle, x: float, y: float) -> None:
    """Draw a yellow moon."""
    moon.speed(MAX_SPEED)
    moon.color("yellow")
    moon.fillcolor("yellow")
    moon.hideturtle()
    moon.penup()
    moon.goto(x, y)
    moon.pendown()
    moon.begin_fill()
    moon.circle(100)
    moon.end_fill()


def draw_cloud(cloud: Turtle, x: float, y: float, r: float) -> None:
    """Draw a cloud."""
    cloud.speed(MAX_SPEED)
    cloud.color("white")
    cloud.fillcolor("white")
    cloud.hideturtle()
    cloud.penup()
    cloud.goto(x, y)
    cloud.pendown()
    cloud.begin_fill()
    i_cloud: int = 0
    while i_cloud < 5:
        cloud.circle(r)
        cloud.forward(uniform(r / 6, r / 3))
        cloud.right(90)
        i_cloud += 1
    cloud.end_fill()


def draw_milky(milky: Turtle, x: float, y: float) -> None:
    """Draw the milky way."""
    milky.speed(MAX_SPEED)
    colormode(255)
    milky.color(2, 241, 224)
    milky.fillcolor(2, 241, 224)
    milky.hideturtle()
    milky.penup()
    milky.goto(x, y)
    milky.pendown()
    milky.pensize(50)
    milky.begin_fill()
    milky.circle(1200, 650)
    milky.end_fill()


def star_generator(scene: Turtle) -> None:
    """Generate Star."""
    x: float = 0.0
    y: float = 0.0
    w: float = 0.0
    i: int = 0
    star_amount: int = randint(80, 150)
    while i < star_amount:
        x = uniform(-700, 700)
        y = uniform(-500, 500)
        w = uniform(15, 50)
        draw_star(scene, x, y, w)
        i += 1
    i = 0


def cloud_generator(scene: Turtle) -> None:
    """Generate Could."""
    x: float = 0.0
    y: float = 0.0
    w: float = 0.0
    i: int = 0
    cloud_amount: int = randint(3, 8)
    while i < cloud_amount:
        x = uniform(-700, 700)
        y = uniform(-50, 500)
        w = uniform(15, 50)
        draw_cloud(scene, x, y, w)
        i += 1
    i = 0


if __name__ == "__main__":
    main()