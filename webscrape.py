import requests
from bs4 import BeautifulSoup, NavigableString
import re
# inspired by Sonia Joseph: https://github.com/soniajoseph/goodreads-quotes/blob/master/scraper.py


def quotes_by_author(author, page_num):

    old_author = author

    author = author.replace(" ", "+")

    all_quotes = []

    # for each page
    for i in range(1, page_num+1, 1):

        try:
            page = requests.get("https://www.goodreads.com/quotes/search?commit=Search&page=" +
                                str(i) + "&q=" + author + "&search[source]=goodreads&search_type=quotes&tab=quotes&utf8=%E2%9C%93")
            soup = BeautifulSoup(page.text, 'html.parser')
            print("scraping page", i)
        except:
            print("could not connect to goodreads")
            break

        try:
            quote = soup.find(class_="leftContainer")
            quote_list = quote.find_all(class_="quoteDetails")
        except:
            pass

        # get data for each quote
        for quote in quote_list:

            meta_data = []

            # Get quote's text
            try:
                outer = quote.find(class_="quoteText").getText()
                # inner_text = [element for element in outer if isinstance(
                #     element, NavigableString)]
                # inner_text = [x.replace("\n", "") for x in inner_text]
                # final_quote = "\n".join(inner_text[:-4])
                # meta_data.append(final_quote.strip())
                outer = str([outer.replace("\n", "")])
                pattern = r'\“(.*?)\”'
                m = re.search(pattern, outer)
                final = m.group()

                if len(final) < 80:
                    all_quotes.append(final)
            except:
                pass

        for text in all_quotes:
            print(text)
            print()

    return all_quotes


quotes_by_author("Napoleon Bonaparte", 1)
