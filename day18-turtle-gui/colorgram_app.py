import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 6)


def get_rgb_colors():
    c = [(colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b) for i in range(len(colors))]
    return c

