from src.imageWriter import MyImageWriter
from src.authorGenerator import getRandomAuthor
from src.instaPublisher import InstaPublisher
author, imgPath = getRandomAuthor()
imageWriter = MyImageWriter(author, imgPath)
imageWriter.drawQuote()
imageWriter.showImage()
imageWriter.saveImage()

insta = InstaPublisher()

caption = "testing functionality"
insta.publish("./tmp/tmpImage.jpg", caption=caption)
