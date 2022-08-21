from cgitb import text
from PIL import Image, ImageDraw, ImageFont
import textwrap

VERT_OFFSET = 0.66  # static Constant


class MyImageWriter:

    def __init__(self, author) -> None:
        self.image = None
        self.quote = None
        self.author = author
        self.myFont = ImageFont.truetype('fonts/Lobster-Regular.ttf', 48)
        self.img = Image.open('images\\napoleon-bonaparte.jpg')

        self.MAX_W, self.MAX_H = self.img.size

    def drawQuote(self, quote) -> None:
        # Create Local Constants
        vertical_pos = self.MAX_H * VERT_OFFSET
        draw = ImageDraw.Draw(self.img)

        # Create Paragraph From quote Text
        para = textwrap.wrap(quote, width=30)

        current_h, pad = vertical_pos, 10
        for line in para:
            w, h = draw.textsize(line, font=self.myFont)
            print(f"Width w: {w} , height h: {h}")
            draw.text((((self.MAX_W - w) / 2), current_h),
                      line, font=self.myFont)
            current_h += h + pad

        current_h += h + (pad * 2)
        # Draw Author
        w, h = draw.textsize(self.author, font=self.myFont)
        draw.text((((self.MAX_W - w) / 2), current_h),
                  self.author, font=self.myFont)
