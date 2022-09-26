from config import USERNAME, PASSWORD
from instabot import Bot


class InstaPublisher:
    def __init__(self):
        self.bot = Bot()
        self.bot.login(username=USERNAME, password=PASSWORD)

    def publish(self, image, caption) -> None:
        self.bot.upload_photo(image, caption=caption)
