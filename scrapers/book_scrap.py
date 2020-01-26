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

env_path = Path('../') / '.env'
load_dotenv(dotenv_path=env_path)


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
        for link in links:
            book_request = requests.get(base_url + link)
            print(book_request)
    
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