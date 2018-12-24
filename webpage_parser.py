from bs4 import BeautifulSoup
from collections import Counter
import datetime
import tclogger

logger = tclogger.get_logger(__name__)


class PageData:

    def __init__(self, title: str, tags_dict: dict):
        self.title = title
        self.tags_dict = tags_dict
        self.datetime_stamp = datetime.datetime.now().strftime('%d_%m_%YT%H:%M:%S:%f')

    def __pretty_print__(self):
        source = '| TAG : COUNT |'
        sep = '\n|' + '-' * 13 + '|\n'
        for tag, count in self.tags_dict.items():
            current = ' ' + str(tag) + ' : ' + str(count)
            source = source + sep + current
        return 'Page title: ' + self.title + '\n' + source

    def __str__(self):
        return self.__pretty_print__()


def parse(html):
    logger.info('Start parsing web page content')
    if html is not None:
        soup = BeautifulSoup(html, 'html.parser')
        logger.debug('Web page source:\n' + str(soup.prettify()))
        title = soup.find('title')
        tags_results = Counter([i.name for i in soup.find_all(True)])
        tags_dictionary = dict(tags_results)
        page_data = PageData(title.text, tags_dictionary)
        return page_data
    else:
        logger.warn('Warning! Empty page source')
        raise RuntimeWarning('Requested page has empty source')



