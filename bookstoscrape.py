# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Step 1: Define the URL of the website to scrape
url = "https://books.toscrape.com/index.html"

# Step 2: Send an HTTP GET request to fetch the HTML content of the webpage
response = requests.get(url)

# Step 3: Save the HTML content to a local file for further processing
with open('booksfile.html', 'w') as html:
    html.write(response.text)

# Step 4: Open the saved HTML file and parse it using BeautifulSoup
with open('booksfile.html', 'r') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# Step 5: Find all `<article>` tags with the class `product_pod` (each representing a book)
product_pod_list = soup.find_all('article', class_='product_pod')

# Step 6: Initialize an empty list to store book data
data = []

# Step 7: Iterate through each `<article>` tag and extract the book's title and price
for elem in product_pod_list:
    # Extract the title of the book from the `<a>` tag inside `<h3>`
    title = elem.h3.a["title"]
    
    # Extract the price of the book from the `<p>` tag inside the `product_price` div
    # Convert the price string (e.g., '£51.77') to a float, removing the '£' symbol
    price = float((elem.find('div', class_='product_price').p.text).lstrip('Â£'))
    
    # Append the book's title and price as a dictionary to the data list
    data.append({title: price})

# Step 8: Print the list of books with their titles and prices
print(data)














