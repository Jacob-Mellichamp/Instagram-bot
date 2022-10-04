from src.imageWriter import MyImageWriter
from src.authorGenerator import getRandomAuthor
from src.instaPublisher import InstaPublisher
author, imgPath = getRandomAuthor()
imageWriter = MyImageWriter(author, imgPath)
imageWriter.drawQuote()
imageWriter.showImage()
imageWriter.saveImage()

# Posting the Image to Instagram.

caption = """Daily Inspiration to get you through the day  


#quoteOftheDay #philosophy #stoicism #business #starcoding #starquotes #quotes #dailymotivation #motivation"""
insta = InstaPublisher()
insta.publish("./tmp/tmpImage.jpg", caption=caption)
