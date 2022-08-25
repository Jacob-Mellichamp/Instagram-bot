import requests
from bs4 import BeautifulSoup, NavigableString
import re
# inspired by Sonia Joseph: https://github.com/soniajoseph/goodreads-quotes/blob/master/scraper.py



class QuoteWebScraper:

    def __init__(self, author) -> None:
        self.author = author
        self.all_quote = []


    def getQuotes(self, quoteNum):
        author = author.replace(" ", "+")


        # for each page
        page_num = 1
        while len(self.all_quotes) < quoteNum:
            try:
                page = requests.get("https://www.goodreads.com/quotes/search?commit=Search&page=" +
                                    str(page_num) + "&q=" + author + "&search[source]=goodreads&search_type=quotes&tab=quotes&utf8=%E2%9C%93")
                soup = BeautifulSoup(page.text, 'html.parser')
                print("scraping page", page_num)
            except:
                print("could not connect to goodreads")
                return self.all_quotes

            #Grab Quote Block
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

                    if len(final) < 80:
                        self.all_quotes.append(final)
                except:
                    pass
            page_num += 1
        return self.all_quotes

    def __str__(self) -> str:
        print("Quotes in List: ")
        print(self.all_quote)
    # def quotes_by_author(self, page_num):

        # old_author = author

        # author = author.replace(" ", "+")

        # all_quotes = []

        # # for each page
        # for i in range(1, page_num+1, 1):

        #     try:
        #         page = requests.get("https://www.goodreads.com/quotes/search?commit=Search&page=" +
        #                             str(i) + "&q=" + author + "&search[source]=goodreads&search_type=quotes&tab=quotes&utf8=%E2%9C%93")
        #         soup = BeautifulSoup(page.text, 'html.parser')
        #         print("scraping page", i)
        #     except:
        #         print("could not connect to goodreads")
        #         break

        #     try:
        #         quote = soup.find(class_="leftContainer")
        #         quote_list = quote.find_all(class_="quoteDetails")
        #     except:
        #         pass

        #     # get data for each quote
        #     for quote in quote_list:

        #         meta_data = []

        #         # Get quote's text
        #         try:
        #             outer = quote.find(class_="quoteText").getText()
        #             # inner_text = [element for element in outer if isinstance(
        #             #     element, NavigableString)]
        #             # inner_text = [x.replace("\n", "") for x in inner_text]
        #             # final_quote = "\n".join(inner_text[:-4])
        #             # meta_data.append(final_quote.strip())
        #             outer = str([outer.replace("\n", "")])
        #             pattern = r'\“(.*?)\”'
        #             m = re.search(pattern, outer)
        #             final = m.group()

        #             if len(final) < 80:
        #                 all_quotes.append(final)
        #         except:
        #             pass

        #     for text in all_quotes:
        #         print(text)
        #         print()

        # return all_quotes


    #quotes_by_author("Napoleon Bonaparte", 1)
