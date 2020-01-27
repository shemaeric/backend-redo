import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import json
import logging
from pprint import pprint
from time import sleep
import uuid
import time
from pymongo import MongoClient
import uuid
from datetime import datetime

env_path = Path('../') / '.env'
load_dotenv(dotenv_path=env_path)

# create connection with mongoDB

DATABASE = os.getenv('DATABASE')

client = MongoClient()

db = client[DATABASE]

table = db['book_book']


def get_urls(url):

    
    try:
        site_request = requests.get(url)
        soup = BeautifulSoup(site_request.content, "html5lib")
        get_individual_book = soup.find_all('a', class_ = "ga-event")
        links = []

        for book in get_individual_book:
            url = book['href']
            if url.startswith('/books/') is True and url[7].isdigit():
                links.append(url)
        
        return links
    
    except Exception as e:
        print('error', e) 


def scrape_book(url, base_url):
    print('url', url)

    try:
        links = get_urls(url)
        data = []
        for link in links:
            book_request = requests.get(base_url + link)
            soup = BeautifulSoup(book_request.content, 'html5lib')
            book_details_section = soup.find_all('section', itemtype = 'http://schema.org/Product')
            data_dict = dict()

            for detail in book_details_section:
                id_section = uuid.uuid4().hex
                data_dict['id'] = id_section
                data_dict['uuid'] = id_section
                data_dict['title'] = detail.find('span', itemprop = 'name').text
                data_dict['main_image'] = detail.find('img', id="product-cover-image")['src']
                price = detail.find('dl', class_="price")
                data_dict['price'] = int(price.find('span', class_ = None).text)
                description = detail.find('div', itemprop = 'description')
                if description is None:
                    data_dict['description'] = ''
                else:
                    text = description.find('p', class_ = None)
                    if text is None:
                       data_dict['description'] = ''
                    else:
                         data_dict['description'] = description.find('p', class_ = None).text
                data_dict['created_at'] = str(datetime.now().time())
                    
            # Insert the data in database.
            table.insert(data_dict)
    
    except Exception as e:
        print('error', e)

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)

    # Get the Web URL from .env
    WEB_LINK = os.getenv("WEB_LINK")
    WEB_LINK_BASE = os.getenv("WEB_LINK_BASE")
    request = requests.get(WEB_LINK)
    if request.status_code == 200:
        scrape_book(WEB_LINK, WEB_LINK_BASE)