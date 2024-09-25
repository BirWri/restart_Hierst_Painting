import random

import colorgram
from turtle import Turtle, Screen
import turtle as t


def extract_colors_from_image():
    """ Extract colors from an image"""
    colors = colorgram.extract('pikachu.jpg', 10)
    return colors


def colors_to_rgb_format(colors):
    """Transform the extracted data to a list of tuples for rgb"""
    list_of_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        list_of_colors.append(new_color)
    return list_of_colors

# Extract colors from chosen image (Doesnt need to be ran every time)
#colors = extract_colors_from_image()
#rgb = colors_to_rgb_format(colors)

#image_color_list =[(178, 159, 17), (23, 56, 24), (123, 116, 14), (249, 213, 52), (41, 92, 17), (245, 169, 28), (70, 102, 10), (253, 239, 192), (240, 75, 31), (58, 118, 18
#)]


# Configure screen and set the correct screen size. The requirements are 10 dots of 20 with 50 in between
canvas_size = (10*20) + (9*50) + 10
print(canvas_size)
screen = Screen()
screen.screensize(canvas_size, canvas_size)


# Configure Painter and add it to correct position
painter = t.Turtle()
painter.hideturtle()
painter.penup()
painter.shape("arrow")
painter.color("black")
painter.setx(-315)
painter.sety(-315)
painter.showturtle()
painter.pendown()
t.colormode(255)


# Create Turtle move function
def move_painter():
    painter.penup()
    painter.forward(70)
    painter.pendown()


# Draw a circle
def draw_filled_circle():
    image_color_list = [(178, 159, 17), (23, 56, 24), (123, 116, 14), (249, 213, 52), (41, 92, 17), (245, 169, 28),
                        (70, 102, 10), (253, 239, 192), (240, 75, 31), (58, 118, 18)]

    painter.dot(20, random.choice(image_color_list))


# Go to new row
def new_row():
    painter.hideturtle()
    painter.penup()
    painter.sety(painter.ycor()+70)
    painter.setx(-315)
    painter.pendown()
    painter.showturtle()


#dot_counter = 0
for dot_counter in range(100):

    if dot_counter % 10 == 0:
        new_row()

    draw_filled_circle()
    move_painter()
    dot_counter += 1


# Canvas only closed when user clicks on it
screen.exitonclick()





