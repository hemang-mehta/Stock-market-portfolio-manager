import requests
from bs4 import BeautifulSoup
import extract_token

def parsePrice(stock_name):
    # Format the stock name to match Yahoo Finance URL format
    url = f"https://finance.yahoo.com/quote/{stock_name}.NS?p={stock_name}.NS"
    print(f'URL -> {url}')
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the 'fin-streamer' element
        fin_streamer_element = soup.find('fin-streamer', class_='Fw(b) Fz(36px) Mb(-4px) D(ib)')

        if fin_streamer_element:
            # Extract the text containing the price
            price = fin_streamer_element.text
            print("Current Stock Price:", price)
        else:
            print("fin-streamer element not found on the page.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# use the extract_token file to access the token name for the stock input by the user
stock_name = extract_token.get_name()
if stock_name == None:
    print('No such stock present.')
else:
    parsePrice(stock_name)
