# This allows me to fetch the content of a web page using requests
import requests

# 'BeautifulSoup' allows me to search through the HTML content of the page and extract the information I want
from bs4 import BeautifulSoup

# Pandas is a library that allows me to organize data into a table and save it as CSV
import pandas as pd

# Time is a library that allows me to pause the program for a few seconds to avoid overwhelming the server with requests
import time

# This is an empty basket to collect books from all pages
all_books = []

# Here I loop through page numbers 1 to 50
for page_number in range(1, 51):

    if page_number == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"

    # This lets me know which page I am currently on
    print(f"Scraping page {page_number}... ({url})")

    # Here I fetch the content of the page using requests
    response = requests.get(url)
    response.encoding = "utf-8"  # Set the encoding to UTF-8 to handle special characters

    # Then I create a BeautifulSoup object and specify the parser
    soup = BeautifulSoup(response.text, "html.parser")

    # Now I use the soup object to search through the HTML and find all books on the page
    books = soup.find_all("article", class_="product_pod")

    # Here I loop through each book on this page and extract its details
    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        stock = book.find("p", class_="instock availability").text.strip()

        # Here I add the book's details into my big basket
        all_books.append({
            "Title": title,
            "Price": price,
            "Stock": stock
        })

    # I pause for half a second to avoid overwhelming the server with requests
    time.sleep(0.5)

# After the loop finishes (all 50 pages done), I convert everything to a table
df = pd.DataFrame(all_books)

# Here I show how many books were collected in total
print(f"\nTotal books collected: {len(df)}")

# Here I preview the first few rows
print(df.head())

# Finally, I save the table as a CSV file
df.to_csv("all_books.csv", index=False)
print("\nData saved to all_books.csv")