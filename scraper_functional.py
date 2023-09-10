import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_soup(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'lxml')

def get_data(soup):
    box = soup.find('div', class_='_1YokD2 _3Mn1Gg')
    
    d = {'title': [], 'price': [], 'rating': [], 'reviews': [], 'delivery': [], 'discount': []}
    
    titles = box.find_all('a', class_='s1Q9rs')
    for title in titles:
        d['title'].append(title.text)
    
    all_prices = box.find_all('div', class_='_30jeq3')
    for price in all_prices:
        d['price'].append(price.text)
    
    all_discounts = box.find_all('div', class_='_3Ay6Sb')
    for discount in all_discounts:
        d['discount'].append(discount.text)
    
    all_deliveries = box.find_all('div', class_='_2Tpdn3')
    for delivery in all_deliveries:
        single_delivery = delivery.text
        if single_delivery not in ['Hot Deal', 'Daily Saver']:
            d['delivery'].append(single_delivery)
    
    specific_divs = box.find_all('div', class_='_4ddWXP')
    for specific_div in specific_divs:
        span_element = specific_div.find('div', class_='_3LWZlK')
        single_rating = span_element.text if span_element else 'No ratings'
        single_rating = single_rating.replace('(', '').replace(')', '')
        d['rating'].append(single_rating)
    
    for specific_div in specific_divs:
        review_span = specific_div.find('span', class_='_2_R_DZ')
        single_review = review_span.text if review_span else 'No reviews'
        single_review = single_review.replace('(', '').replace(')', '')
        d['reviews'].append(single_review)
    
    return d

def write_to_csv(data, filename):
    flipkart_df = pd.DataFrame.from_dict(data)
    flipkart_df.to_csv(filename, header=True, index=False)

def main(url, filename):
    soup = get_soup(url)
    data = get_data(soup)
    write_to_csv(data, filename)
    print('\nCSV uploaded')

if __name__ == "__main__":
    url = 'https://www.flipkart.com/search?q=garlic%20press&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    filename = "flipkart_data.csv"
    main(url, filename)
