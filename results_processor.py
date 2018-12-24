import requests
import webpage_parser
import db_module
import re
import tagcounter_config
import tclogger


logger = tclogger.get_logger(__name__)


def process_url(get_param: str):
    logger.info('Start processing site=' + get_param)
    url = tagcounter_config.get_url(get_param)
    if url is None:
        url = __format_url__(get_param)
    html = http_get(url)
    page_data = webpage_parser.parse(html)
    page_data.base_url = url
    return page_data


def show_results(view_param: str):
    logger.info('Show results for url = ' + view_param)
    url = tagcounter_config.get_url(view_param)
    if url is None:
        url = __format_url__(view_param)
    page_data = db_module.show_from_db(url)
    return page_data


def http_get(url: str):
    logger.info('HTTP: GET ' + url)
    response = requests.get(url)
    if response.status_code is not 200:
        raise RuntimeError('HTTP Error. Response status code is: ' + response.status_code)
    return response.content


def __format_url__(user_input: str):
    logger.info('Validating input against URL mask')
    pattern = '(https{0,1}://){0,1}[a-zA-Z0-9]+[.]{1}[a-zA-Z0-9]+'
    match1 = re.match(pattern, user_input)
    if match1 is not None:
        print(match1.group(1))
        scheme = match1.group(1)
        if scheme is not None:
            url = user_input
        else:
            url = 'http://' + user_input
        logger.info('Validation passed. URL=' + url)
        return url
    else:
        raise RuntimeError('Please set the correct url')











