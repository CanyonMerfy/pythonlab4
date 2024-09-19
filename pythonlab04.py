import turtle




# Create a turtle object
t = turtle.Turtle()

# Hide the turtle and set speed
t.speed(10)  # 1 is slow, 10 is fast, 0 is instant


# Create a window to draw in
# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("darkblue")
# Set the width and height of the screen
screen.setup(width=600, height=600)
# Clear the screen
t.clear()


def draw_square(t, length):
    for _ in range(4):
        t.forward(length)
        t.left(90)



def draw_circle(t, radius):
    t.circle(radius)


def draw_polygon(t, sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)





def get_stem_position(x, y, radius):
    diameter = radius * 2
    x_pos = x + 10
    y_pos = y + diameter - 10
    pos = (x_pos, y_pos)
    return pos


def get_eye_position(x, y, radius, eye_number, size):
    diameter = radius * 2
    x_pos = ((diameter / 3) * eye_number) - (size / 2) + x
    y_pos = radius + y
    xy_pos = (-radius + x_pos, y_pos)
    return xy_pos

def get_mouth_position(x, y, width, radius):
    diameter = radius * 2
    x_pos = x - (width / 2)
    y_pos = y + diameter / 3
    xy_pos = (x_pos, y_pos)
    return xy_pos

def draw_pumpkin(t, x, y, radius):
    pumpkin_radius = radius
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    # Drawing the stem
    t.penup()
    t.goto(get_stem_position(x, y, radius))
    t.pendown()
    t.fillcolor("green")
    t.begin_fill()

    t.left(90)  # Point upwards
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.end_fill()


def draw_eye(t, x, y, size, pump_radius, eye_number):
    t.penup()
    t.goto(get_eye_position(x, y, pump_radius, eye_number, size))
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_mouth(t, x, y, width, pump_radius):
    t.penup()
    t.goto(get_mouth_position(x, y, width, pump_radius))
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.right(60)
    for _ in range(5):  # Create a simple zigzag mouth
        t.forward(width // 5)
        t.left(120)
        t.forward(width // 5)
        t.right(120)
    t.end_fill()
    t.left(60)


def draw_jackolantern(t, x, y, eye_size, mouth_width, radius):
    draw_pumpkin(t, x, y, radius)  # Draw the pumpkin
    draw_eye(t, x, y, eye_size, radius, 1)  # Left eye
    draw_eye(t, x, y, eye_size, radius, 2)  # Right eye
    draw_mouth(t, x, y, mouth_width, radius)  # Mouth






def draw_star(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)  # 144 degrees is the angle to form a star
    t.end_fill()



import random
def draw_sky(t, num_stars):
    for _ in range(num_stars):
        x = random.randint(-200, 300)
        y = random.randint(0, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)



draw_jackolantern(t, -150, -300, 30, 100, 100)
draw_jackolantern(t, 0, -300, 25, 60, 80)
draw_jackolantern(t, 150, -300, 30, 80, 100)

draw_sky(t, 200)








# Close the turtle graphics window when clicked
turtle.exitonclick()



