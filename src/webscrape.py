from distutils.log import error
import requests
from bs4 import BeautifulSoup, NavigableString
import re
import random
import os.path
# inspired by Sonia Joseph: https://github.com/soniajoseph/goodreads-quotes/blob/master/scraper.py


class QuoteWebScraper:

    MAX_STRING_LENGTH = 80
    # Scrapper constructor

    def __init__(self, author) -> None:
        self.author = author
        self.all_quotes = []

    # Param: quoteNum <Integer>: amount of quotes to fetch from goodreads.
    # Pre: NA
    # Post: all_quotes list is declared with 'quoteNum' amount of quotes

    def getQuotes(self, quoteNum):
        new_author = self.author.replace(" ", "+")

        # check for file if it exist before webscraping
        fileExist = self.checkQuoteFile()

        if fileExist:
            self.readQuotesFromFile()
            return self.all_quotes

        # for each page
        page_num = 1
        while len(self.all_quotes) < quoteNum:
            try:
                page = requests.get("https://www.goodreads.com/quotes/search?commit=Search&page=" +
                                    str(page_num) + "&q=" + new_author + "&search[source]=goodreads&search_type=quotes&tab=quotes&utf8=%E2%9C%93")
                soup = BeautifulSoup(page.text, 'html.parser')
                print("scraping page", page_num)
            except:
                print("could not connect to goodreads")
                return self.all_quotes

            # Grab Quote Block
            try:
                quote = soup.find(class_="leftContainer")
                quote_list = quote.find_all(class_="quoteDetails")
            except:
                pass

            # get data for each quote
            for quote in quote_list:
                # Get quote's text
                try:
                    outer = quote.find(class_="quoteText").getText()
                    outer = str([outer.replace("\n", "")])
                    pattern = r'\“(.*?)\”'
                    m = re.search(pattern, outer)
                    final = m.group()

                    if len(final) < self.MAX_STRING_LENGTH:
                        self.all_quotes.append(final)
                except:
                    pass
            page_num += 1
        print(self.all_quotes)
        self.writeToFile()  # cache contents of the quote list
        return self.all_quotes

    def __str__(self) -> str:
        output = ""
        for text in self.all_quotes:
            output += str(text) + "\n"
        return output

    # Post: return a random Quote
    def getRandomQuote(self):
        return random.choice(self.all_quotes)

    # Post: write the contents of quotes to a file, each line being a different quote.
    def writeToFile(self):
        myFile = open(f"quotes\\{self.author}.txt", "w")
        for quote in self.all_quotes:
            try:
                myFile.write(quote + "\n")
            except:
                print(f"Error Printing line: {quote}")
        myFile.close()
        return None

    # Post: read quote contents from file if exist, populate self.quotes
    def readQuotesFromFile(self):
        myFile = open(f"quotes\\{self.author}.txt", "r+")
        while True:
            line = myFile.readline()

            if not line:
                break

            self.all_quotes.append(line.strip())

        myFile.close()
        return None

    # Post: Does a file for the author already exist?
    def checkQuoteFile(self):
        return os.path.exists(f"quotes\\{self.author}.txt")
