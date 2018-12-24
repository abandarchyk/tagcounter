import sqlite3
import pickle
from webpage_parser import PageData

# todo connection management


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS scan_results(site_name TEXT, site_url TEXT, scan_timestamp TEXT,'
              ' tags BLOB)')
    conn.commit()


conn = sqlite3.connect('db/scan_results.db')
c = conn.cursor()
create_table()


def close():
    c.close()
    conn.close()


def save_results(site_name, site_url, scan_timestamp, tags: dict):
    serialized_tags_dict = pickle.dumps(tags)
    c.execute('INSERT INTO scan_results(site_name, site_url, scan_timestamp, tags) VALUES (?, ?, ?, ?)',
              (site_name, site_url, scan_timestamp, sqlite3.Binary(serialized_tags_dict)))
    conn.commit()


def show_from_db(site_url):
    c.execute('SELECT site_name, tags FROM scan_results WHERE site_url="' + site_url + '"')
    data = c.fetchall()
    conn.commit()
    site_name = data[0][0]
    tags_pickled = data[0][1]
    tags_unpickled = pickle.loads(tags_pickled)
    page_data = PageData(site_name, tags_unpickled)
    return page_data




