import random
from time import time
authors = [
    ("Napoleon Bonaparte", 'images\\napoleon-bonaparte.jpg'),
    ("Marcus Aurelius", 'images\\marcus-aurelius.jpg'),
    ("Andrew Carnegie", 'images\\andrew-carnegie.jpg'),
    ("Henry Ford", 'images\\henry-ford.jpg'),
    ("Thomas Edison", 'images\\thomas-edison.jpg'),
    ("Walt Disney", 'images\\walt-disney.jpg')
]


def getRandomAuthor():
    return random.choice(authors)
