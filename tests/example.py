from cgitb import text
from PIL import Image, ImageDraw, ImageFont
import textwrap
img = Image.open('images\\napoleon-bonaparte.jpg')

image_text = "\"Whatever the mind of men can conceive and believe it can achieve\" - "
image_buffer = "---------------"
image_author = "Napolean Bonaparte"
# Get the size of the image
size = img.size
MAX_W, MAX_H = size[0], size[1]


# Get Positioning
horzitonal_pos = size[0] * 0.75
vertical_pos = size[1] * 0.66

#print(f"{horzitonal_pos} , {vertical_pos}")


# Text Wrap
para = textwrap.wrap(image_text, width=30)

# Get Font
myFont = ImageFont.truetype('fonts/IBMPlexSerif-Regular.ttf', 48)
myAuthorFont = ImageFont.truetype('fonts/IBMPlexSerif-Italic.ttf', 48)
# Display Image


draw = ImageDraw.Draw(img)

# Draw Quote on Image
current_h, pad = vertical_pos, 10
for line in para:
    w, h = draw.textsize(line, font=myFont)
    print(f"Width w: {w} , height h: {h}")
    draw.text((((MAX_W - w) / 2), current_h), line, font=myFont)
    current_h += h + pad


current_h += h + (pad * 2)
# Draw Author
w, h = draw.textsize(image_author, font=myFont)
draw.text((((MAX_W - w) / 2), current_h), image_author, font=myAuthorFont)
img.show()
# img.save("images/image_text.jpg")
