import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

d = {'title':[],'price':[],'rating':[],'reviews':[],'delivery':[],'discount':[]}
# Prompt the user for the base URL
base_url = input("Enter the base URL you want to scrape: ")

# Define the range of pages you want to scrape
start_page = int(input("Enter the start page: "))
end_page = int(input("Enter the end page: "))

for i in range(start_page, end_page + 1):
    url = f'{base_url}&page={i}'  # Assuming the page parameter is used like this
    print(f'Fetching data from page {i} with URL: {url}')

    response = requests.get(url)

    soup = BeautifulSoup(response.text,'lxml')

    box = soup.find('div',class_ ='_1YokD2 _3Mn1Gg')

    new_page = soup.find('a',class_ = '_1LKTO3').get('href')

    full_link = 'https://www.flipkart.com' + new_page 

    titles = box.find_all('a', class_ = 's1Q9rs')

    for title in titles:
        single_title = title.text
        d['title'].append(single_title)

    all_prices = box.find_all('div', class_ = '_30jeq3')

    for price in all_prices:
        single_price = price.text
        d['price'].append(single_price)

    # all_discounts = box.find_all('div', class_ = '_3Ay6Sb')

    # for discount in all_discounts:
    #     single_discount = discount.text
    #     d['discount'].append(single_discount)          

    specific_divs = box.find_all('div', class_='_4ddWXP')

    for specific_div in specific_divs:
        # Check if a span element is present inside each div
        span_element = specific_div.find('div', class_='_3LWZlK')

        if span_element:
            single_rating = span_element.text
            single_rating = single_rating.replace('(', '').replace(')', '')  # Remove round parentheses
            d['rating'].append(single_rating)
        else:
            d['rating'].append('No ratings')

    for specific_div in specific_divs:
        # Check if a span element is present inside each div
        review_span = specific_div.find('span', class_='_2_R_DZ')

        if review_span:
            single_review = review_span.text
            single_review= single_review.replace('(', '').replace(')', '')  # Remove round parentheses
            d['reviews'].append(single_review)
        else:
            d['reviews'].append('No reviews')

    for specific_div in specific_divs:
        # Check if a span element is present inside each div
        delivery_span = specific_div.find('div', class_='_2Tpdn3')

        if delivery_span:
            single_delivery = delivery_span.text
            single_delivery = single_delivery.replace('(', '').replace(')', '')  # Remove round parentheses
            d['delivery'].append(single_delivery)
        else:
            d['delivery'].append('No delivery')  
    
    for specific_div in specific_divs:
        # Check if a span element is present inside each div
        discount_span = specific_div.find('div', class_='_3Ay6Sb')

        if discount_span:
            single_discount= discount_span.text
            single_discount = single_discount.replace('(', '').replace(')', '')  # Remove round parentheses
            d['discount'].append(single_discount)
        else:
            d['discount'].append('No discount')   
    
    print(f'Length of titles after page {i}: {len(d["title"])}')
    print(f'Length of prices after page {i}: {len(d["price"])}')
    print(f'Length of ratings after page {i}: {len(d["rating"])}')
    print(f'Length of reviews after page {i}: {len(d["reviews"])}')
    print(f'Length of delivery after page {i}: {len(d["delivery"])}')
    print(f'Length of discounts after page {i}: {len(d["discount"])}')

loading_chars = ['|', '/', '-', '\\']

print('Preparing CSV')

for _ in range(10):  # Adjust the range based on your preference
    for char in loading_chars:
        print(f'\rLoading... {char}', end='', flush=True)
        time.sleep(0.1)  # Adjust the sleep duration for desired animation speed

flipkart_df = pd.DataFrame.from_dict(d)
flipkart_df.to_csv("flipkart_data.csv", header=True, index=False)
print('\nCSV uploaded')
