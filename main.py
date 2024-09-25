import colorgram


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


colors = extract_colors_from_image()
rgb = colors_to_rgb_format(colors)
print(rgb)

