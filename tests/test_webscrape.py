
from src.webscrape import QuoteWebScraper

myQuotes = QuoteWebScraper("Napoleon Bonaparte")

myQuotes.getQuotes(16)

assert(len(myQuotes.all_quotes), 16)
rand = myQuotes.getRandomQuote()

print(rand)
