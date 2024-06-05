import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

# URL of website to scrape
Base_URL = 'http://books.toscrape.com'


# Function to scrape a page
def scrape_page(page_number):
    try:
        # Get request to the website
        url = Base_URL + '/catalogue/page-' + str(page_number) + '.html'
        response = requests.get(url)
        response.raise_for_status()

    # If an HTTP error occurred (e.g., 404 Not Found, 500 Internal Server
    # Error),  print the error and return None
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
        return None

    # If a connection error occurred (e.g., network problem), print
    # the error and return None
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        return None

    # If a timeout error occurred (i.e., the request took too long),
    # print the error and return None
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        return None

    # If any other type of error occurred with the request, print
    # the error and return None
    except requests.exceptions.RequestException as err:
        print("Something went wrong with the request:", err)
        return None

    # Parses the HTML Content
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


# Function to extract the data (books) from the page
def extract_data(soup):
    if soup is None:
        print("No data to process")
        return []

    # List to store the books
    books = []
    # Loop through the books
    try:
        for book in soup.find_all('article', class_='product_pod'):
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            availability = (book.find('p', class_='instock availability')
                            .text.strip())
            book_url = urljoin(Base_URL, book.h3.a['href'])
            image_url = urljoin(Base_URL, book.img['src'])
            star_rating = book.find('p', class_='star-rating')['class'][1]
            books.append([
                title,
                price,
                availability,
                book_url,
                image_url,
                star_rating
            ])
    except AttributeError as e:
        print("Error while parsing the HTML:", e)
    return books


# Scrape multiple pages
def scrape_multiple_pages(pages):
    all_books = []
    for page_number in range(1, pages+1):
        soup = scrape_page(page_number)
        books = extract_data(soup)
        all_books.extend(books)
    return all_books


# Create a DataFrame
books = scrape_multiple_pages(50)
df = pd.DataFrame(books, columns=['Title', 'Price', 'Availability', 'URL',
                                  'Image URL', 'Star Rating'])

# Saving the DataFrame to a csv file called 'books.csv'
df.to_csv('books.csv', index=False)
