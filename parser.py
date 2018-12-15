from bs4 import BeautifulSoup
from collections import Counter
import datetime
import pickle
import sqlite3
import logging
import sys

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


with open('html_test.txt', 'r', encoding='UTF-8') as file:
    soup = BeautifulSoup(file, 'html.parser')
    logging.info('Response received:')
    logging.debug(soup.prettify())


tags_results = Counter([i.name for i in soup.find_all(True)])
tags_dictionary = dict(tags_results)
print('Result dict')
print(tags_dictionary)

logging_filename = datetime.datetime.now().strftime('%d_%m_%YT%H:%M:%S:%f')

# PICKLE
with open('pickled_file', 'wb') as result_file:
    s = pickle.dump(tags_dictionary, result_file)
    print(s)
    type(s)
    print()


with open('pickled_file', 'rb') as pickled:
    new_dict = pickle.load(pickled)
    print('UNPICLED')
    print(new_dict)
    print(new_dict == tags_dictionary)

# SQLite
# имя сайта, url, дата проверки, данные о тэгах. sqlite.Binary(file)

conn = sqlite3.connect('example.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS crawling_results(site_name TEXT, site_url TEXT, scan_timestamp TEXT,'
              ' tags BLOB)')
    conn.commit()


def insert_to_table(site_name, site_url, scan_timestamp, tags):
    c.execute('INSERT INTO crawling_results(site_name, site_url, scan_timestamp, tags) VALUES (?, ?, ?, ?)',
              (site_name, site_url, scan_timestamp, tags))
    conn.commit()


def read_from_table():
    c.execute('SELECT site_url, scan_timestamp, tags FROM crawling_results WHERE site_name="tut.by"')
    data = c.fetchall()
    print(data[0][0])
    print(data[0][1])
    print(data[0][2])
    res = pickle.loads(data[0][2])
    print(res)


create_table()

bina = pickle.dumps(tags_dictionary)
insert_to_table('tut.by', 'https://tut.by/', logging_filename, sqlite3.Binary(bina))

read_from_table()




c.close()
conn.close()
