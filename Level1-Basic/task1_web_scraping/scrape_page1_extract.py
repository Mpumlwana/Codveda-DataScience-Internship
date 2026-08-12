# 'requests' lets us fetch the webpage
import requests

# 'BeautifulSoup' lets us search through the HTML we get back
from bs4 import BeautifulSoup

# 'pandas' lets us organize data into a table and save it as CSV
import pandas as pd

# The page I want to scrape (just page 1)
url = "https://books.toscrape.com/"

# I am fetching the page
response = requests.get(url)
response.encoding = "utf-8"

# Here I turn the raw HTML into a searchable "soup" object
soup = BeautifulSoup(response.text, "html.parser")

# I am finding every book listing on the page
books = soup.find_all("article", class_="product_pod")

print("Number of books found on this page:", len(books))

# An empty list where I will collect each book's details
all_books = []

# Here I loop through each book box and pull out its details
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    stock = book.find("p", class_="instock availability").text.strip()

    #I am storing this book's info as a dictionary
    all_books.append({
        "Title": title,
        "Price": price,
        "Stock": stock
    })

#Now I am converting my list of dictionaries into a pandas DataFrame (a table)
df = pd.DataFrame(all_books)

# Here I show the table in the terminal, so we can see it before saving
print("\n--- Preview of the table ---")
print(df)

#Here I Save the table to a CSV file
df.to_csv("books_page1.csv", index=False)

print("\nData saved to books_page1.csv")