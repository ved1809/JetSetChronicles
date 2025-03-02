import turtle
import math

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Solar System")

# Create the Sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(stretch_wid=3, stretch_len=3)  # Make the Sun larger

# Create Earth
earth = turtle.Turtle()
earth.shape("circle")
earth.color("blue")
earth.penup()
earth.goto(100, 0)
earth.pendown()

# Create Moon
moon = turtle.Turtle()
moon.shape("circle")
moon.color("gray")
moon.penup()
moon.goto(120, 0)
moon.pendown()

# Move the Earth and Moon in orbit around the Sun
def move_planets():
    angle_earth = 0
    angle_moon = 0
    while True:
        # Earth orbiting the Sun
        x_earth = 100 * math.cos(math.radians(angle_earth))
        y_earth = 100 * math.sin(math.radians(angle_earth))
        earth.goto(x_earth, y_earth)

        # Moon orbiting the Earth
        x_moon = x_earth + 20 * math.cos(math.radians(angle_moon))
        y_moon = y_earth + 20 * math.sin(math.radians(angle_moon))
        moon.goto(x_moon, y_moon)

        angle_earth += 1
        angle_moon += 5

# Start the animation
move_planets()

# Keep the window open
wn.mainloop()
