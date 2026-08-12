import requests

# This is the web address (URL) of the page I want to scrape
url = "https://books.toscrape.com/"

response = requests.get(url)

# Print the status code of the response
print("Status Code:", response.status_code)  

# To peek the first 500 characters of the raw HTML and response to prove that I recieved the page content.
print("\n--- First 500 characters of the page content ----")
print(response.text[:500])