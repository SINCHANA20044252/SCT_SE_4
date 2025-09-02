import requests
from bs4 import BeautifulSoup
import csv

# URL of the site
URL = "http://books.toscrape.com/"
response = requests.get(URL)

# Parse HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Find all product listings
books = soup.find_all('article', class_='product_pod')

# CSV file to save
with open('books.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Title', 'Price', 'Rating'])

    for book in books:
        # Title
        title = book.h3.a['title']
        
        # Price
        price = book.find('p', class_='price_color').text
        
        # Rating (as word)
        rating_class = book.find('p', class_='star-rating')['class']
        rating = rating_class[1]  # Example: ['star-rating', 'Three']
        
        # Write to CSV
        writer.writerow([title, price, rating])

print("Scraping complete! Data saved to books.csv.")
