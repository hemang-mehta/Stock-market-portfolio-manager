import pandas as pd

def get_name():
    df = pd.read_csv('Learning_Webscraping/Token_names.csv')

    name = input('Enter company name: ')

    # Filter rows where the company name contains 'Reliance'
    reliance_companies = df[df['Company Name'].str.lower().str.contains(name, case=False, na=False)]

    # Check if any matching companies were found
    if not reliance_companies.empty:
        # Access the symbol(s) of the matching company/companies
        symbols = reliance_companies['Symbol'].tolist()

        if len(symbols) == 1:
            print(f"Symbol for the company containing 'Reliance' in its name: {symbols[0]}")
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