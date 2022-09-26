import random
from time import time
authors = [
    ("Napoleon Bonaparte", 'images\\napoleon-bonaparte.jpg'),
    ("Marcus Aurelius", 'images\\marcus-aurelius.jpg'),
    ("Andrew-Carnegie", 'images\\andrew-carnegie.jpg')
]


def getRandomAuthor():
    return random.choice(authors)
