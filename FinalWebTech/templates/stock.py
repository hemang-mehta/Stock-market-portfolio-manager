import requests
from bs4 import BeautifulSoup
import extract_token
import pandas as pd

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

# Use the extract_token file to access the token name for the stock input by the user
stock_name = extract_token.get_name()
if stock_name is None:
    print('No such stock present.')
else:
    parsePrice(stock_name)

def get_name():
    df = pd.read_csv('Token_names.csv')  # Update the path to your CSV file here

    name = input('Enter company name: ')

    # Filter rows where the company name contains 'Reliance'
    reliance_companies = df[df['Company Name'].str.lower().str.contains(name, case=False, na=False)]

    # Check if any matching companies were found
    if not reliance_companies.empty:
        # Access the symbol(s) of the matching company/companies
        symbols = reliance_companies['Symbol'].tolist()

        if len(symbols) == 1:
            print(f"Symbol for the company containing '{name}' in its name: {symbols[0]}")
            return symbols[0]
        else:
            print(f"Symbols for the companies containing '{name}' in their names: {', '.join(symbols)}")
            while True:
                a = input('Select your company: ')
                if a not in symbols:
                    pass
                else:
                    print(f'Returning {a}')
                    return a
    else:
        return None
