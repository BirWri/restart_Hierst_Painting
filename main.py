import colorgram
from turtle import Turtle, Screen


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

image_color_list =[(178, 159, 17), (23, 56, 24), (123, 116, 14), (249, 213, 52), (41, 92, 17), (245, 169, 28), (70, 102, 10), (253, 239, 192), (240, 75, 31), (58, 118, 18
)]

# Configure screen and set the correct screen size. The requirements are 10 dots of 20 with 50 in between
canvas_size = (10*20) + (9*50)
print(canvas_size)
screen = Screen()
screen.screensize(canvas_size, canvas_size)


# Configure Painter and add it to correct position
painter = Turtle()
painter.hideturtle()
painter.penup()
painter.shape("arrow")
painter.color("black")
painter.setx(-315)
painter.sety(-315)
painter.showturtle()
painter.pendown()

# Canvas only closed when user clicks on it
screen.exitonclick()


# Create Turtle move function



