
from src.webscrape import QuoteWebScraper, quotes_by_author

myQuotes = QuoteWebScraper("Napoleon Bonaparte")

# myQuotes.getQuotes(10)

print(myQuotes)

print(quotes_by_author("Napoleon Bonaparte", 1))
