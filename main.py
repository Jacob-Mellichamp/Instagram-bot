from src.imageWriter import MyImageWriter
from src.authorGenerator import getRandomAuthor

author, imgPath = getRandomAuthor()
imageWriter = MyImageWriter(author, imgPath)
imageWriter.drawQuote()
imageWriter.showImage()
