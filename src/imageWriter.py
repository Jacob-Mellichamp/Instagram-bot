from cgitb import text
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import textwrap

from src.webscrape import QuoteWebScraper

VERT_OFFSET = 0.66  # static Constant
QUOTE_NUMBER = 26   # Number of possible random quotes
CONTRAST_FACTOR = 0.5  # contrast multiplyer


class MyImageWriter:

    def __init__(self, author) -> None:
        # Load Defaults
        self.myFont = ImageFont.truetype('fonts/IBMPlexSerif-Regular.ttf', 48)
        self.img = Image.open('images\\napolean-bonaparte-adjusted.png')
        self.MAX_W, self.MAX_H = self.img.size

        # Get Quote From Webscraper
        self.quoteScraper = QuoteWebScraper(author)
        self.quoteScraper.getQuotes(QUOTE_NUMBER)
        self.quote = self.quoteScraper.getRandomQuote()

    def drawQuote(self) -> None:

        # Create Local Constants
        vertical_pos = self.MAX_H * VERT_OFFSET
        draw = ImageDraw.Draw(self.img)

        # Create Paragraph From quote Text
        para = textwrap.wrap(self.quote, width=30)

        current_h, pad = vertical_pos, 10
        for line in para:
            w, h = draw.textsize(line, font=self.myFont)
            print(f"Width w: {w} , height h: {h}")
            draw.text((((self.MAX_W - w) / 2), current_h),
                      line, font=self.myFont)
            current_h += h + pad

        current_h += h + (pad * 2)
        # Draw Author
        w, h = draw.textsize(self.quoteScraper.author, font=self.myFont)
        draw.text((((self.MAX_W - w) / 2), current_h),
                  self.quoteScraper.author, font=self.myFont)

    # Show image in your default image viewing application.
    def showImage(self) -> None:
        self.img.show()
