from bs4 import BeautifulSoup
from collections import Counter
import datetime
import pickle
import sqlite3
import logging


# LOGGING

logger = logging.getLogger('cho')

consoleHandler = logging.StreamHandler()
consoleFormatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
consoleHandler.setFormatter(consoleFormatter)
consoleHandler.setLevel(logging.INFO)
logger.addHandler(consoleHandler)


fileHandler = logging.FileHandler('loggi.log')
fileFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileHandler.setFormatter(fileFormatter)
fileHandler.setLevel(logging.DEBUG)
logger.addHandler(fileHandler)


class PageData:

    def __init__(self, title: str, links: list, tags_dict: dict):
        self.title = title
        self.links = links
        self.tags_dict = tags_dict
        self.datetime_stamp = datetime.datetime.now().strftime('%d_%m_%YT%H:%M:%S:%f')

    def __str__(self):
        return 'PAGE DATA TITLE: ' + self.title


def parse(html):
    # assert
    soup = BeautifulSoup(html, 'html.parser')
    # log: soup.prettify()
    title = soup.find('title')
    print(title)
    # link
    hrefs = [link.get('href') for link in soup.find_all('a', href=True)]
    print('HREFS')
    print(hrefs)
    tags_results = Counter([i.name for i in soup.find_all(True)])
    tags_dictionary = dict(tags_results)
    print('Result dict:')
    print(tags_dictionary)

    page = PageData(title.text, hrefs, tags_dictionary)
    return page



