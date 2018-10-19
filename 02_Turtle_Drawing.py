
### Define Draw_shape function

jack = turtle.Turtle()

def draw_shape(length, color, sides):
    jack.color(color)
    for side in range(sides):
        jack.forward(length)
        jack.right(360/sides)

draw_shape(100, "cyan", 5)

### Square flower

import turtle

romeo = turtle.Turtle()
romeo.color("violet")
romeo.width(5)
romeo.speed(8)

juliet = turtle.Turtle()
juliet.color("misty rose")
juliet.speed(8)

def draw_square(some_turtle):
    for side in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_flower(some_turtle):
    for petal in range(6):
        draw_square(some_turtle)
        some_turtle.right(60)
    some_turtle.hideturtle()

draw_flower(romeo)
draw_flower(juliet)


### Draw a heart with two colors


romeo = turtle.Turtle()
juliet = turtle.Turtle()

juliet.color("misty rose")
juliet.width(3)

romeo.color("violet")
romeo.width(3)
romeo.left(40)
romeo.forward(100)

for side in range(185):
    romeo.forward(1)
    romeo.left(1)
romeo.hideturtle()


juliet.left(140)
juliet.forward(100)
for side in range(185):
    juliet.forward(1)
    juliet.right(1)
juliet.hideturtle()

#### Use Modulo for repeating patterns
'''
the modulo operator, %, divides one number by another—and then gives the remainder of that division.
The modulo operation is really useful for doing things that involve cycles or any kind of repating patterns.
'''

# Modulo -- application of two options -- staircase pattern
t = turtle.Turtle()
t.width(5)
t.color("limegreen")

for step in range(21):
  t.forward(10)  # just one!

  # Alternate turning left and right.
  if step % 2 == 0:
    t.left(90)
  else:
    t.right(90)

t.hideturtle()

# Modulo -- application of three options -- three colors alternatively
t = turtle.Turtle()
t.width(5)

for n in range(12):
    t.color("gray")
    if n % 3 == 0:
        t.color("red")
    if n % 3 == 1:
        t.color("orange")
    if n % 3 == 2:
        t.color("yellow")
    t.forward(50)
    t.right(360/12)

### Fizzbuzz quiz

def fizz(tur):
    # A red square bead.
    tur.color("red")
    tur.left(90)
    for side in [10, 20, 20, 20, 10]:
        tur.forward(side)
        tur.right(90)

def buzz(tur):
    # A green hexagonal bead.
    # Fits inside the red bead.
    tur.color("green")
    tur.left(60)
    for side in range(6):
        tur.forward(10)
        tur.right(60)
    tur.right(60)

def plain(tur):
    # A gray octagonal bead.
    tur.color("gray")
    tur.left(90)
    for side in [4, 8, 8, 8, 8, 8, 8, 8, 4]:
        tur.forward(side)
        tur.right(45)
    tur.right(45)

# Set up the turtle to draw beads.
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.penup()
t.back(180)  # Back up to make room!
t.pendown()

for num in range(16):
    if num % 3 == 0:
        fizz(t)
        if num % 5 == 0:
            buzz(t)
    else:
        if num % 5 == 0:
            buzz(t)
        else:
            plain(t)

    # Advance to the next bead spot.
    t.color("gray")
    t.forward(22)
t.hideturtle()