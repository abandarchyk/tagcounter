import sqlite3
import pickle
from webpage_parser import PageData
import tclogger

logger = tclogger.get_logger(__name__)


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
    logger.info('Saving results to DB for: ' + site_name + ' - ' + site_url)
    serialized_tags_dict = pickle.dumps(tags)
    c.execute('INSERT INTO scan_results(site_name, site_url, scan_timestamp, tags) VALUES (?, ?, ?, ?)',
              (site_name, site_url, scan_timestamp, sqlite3.Binary(serialized_tags_dict)))
    conn.commit()


def show_from_db(site_url):
    logger.info('Fetching results from DB by: ' + site_url)
    c.execute('SELECT site_name, tags FROM scan_results WHERE site_url="' + site_url + '"')
    data = c.fetchall()
    conn.commit()
    logger.debug('DB fetched' + str(data))
    site_name = data[len(data)-1][0]
    tags_pickled = data[len(data)-1][1]
    tags_unpickled = pickle.loads(tags_pickled)
    page_data = PageData(site_name, tags_unpickled)
    return page_data




