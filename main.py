import colorgram

colors = colorgram.extract('pikachu.jpg', 6)
print(colors)
list_of_colors = []

#TODO transform the info into a list of just the colors
for x in range(0,len(colors)-1):
    r = colors[x].rgb.r
    g = colors[x].rgb.g
    b = colors[x].rgb.b
    new_color = (r, g, b)
    list_of_colors.append(new_color)

print(list_of_colors)


