import sqlite3
import pickle

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


def show_from_db():
    c.execute('SELECT site_url, scan_timestamp, tags FROM scan_results WHERE site_name="tut.by"')
    data = c.fetchall()
    print(data[0][0])
    print(data[0][1])
    print(data[0][2])
    res = pickle.loads(data[0][2])
    print(res)


