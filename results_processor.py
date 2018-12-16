import requests
import webpage_parser
import db_module
import config


# имя сайта, url, дата проверки, данные о тэгах. sqlite.Binary(file)

def _get_full_url(site: dict):
    scheme = site['scheme']
    host = site['host']
    url = scheme + '://' + host
    print(url)
    return url


def process(site: dict):
    # assert
    full_url = _get_full_url(site)
    response = requests.get(full_url)
    response_content = response.content
    print(response.status_code)
    page = webpage_parser.parse(response_content)
    db_module.save_results(site['name'], full_url, page.datetime_stamp, page.tags_dict)
    return page




