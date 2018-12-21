import sys
import argparse
import logging
import results_processor

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler(sys.stdout)
consoleFormatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
consoleHandler.setFormatter(consoleFormatter)
consoleHandler.setLevel(logging.INFO)
logger.addHandler(consoleHandler)

logger.debug('debug')
logger.info('info')
logger.warning('warning')

#
parser = argparse.ArgumentParser(usage='Available params --get and --view', description='pppppppppppparser')
parser.add_argument('-g', '--get',  help='url to web site page to parse')
parser.add_argument('-v', '--view', help='url to web site page to parse')
#
args = parser.parse_args()


if args.get:
    print('CLI get')
    get = args.get
    #url_executor
    if get in aliases:
        url = get_url(get)
    else:
        url = get
    process(url)


elif args.view:
    print('CLI view')
    print(args.view)
#    db_module.view(url)

else:
    print('Loading GUI')
    GUI()


def process(url):
    results_processor.process(url)

def greetings():
    print('Super Hi %username% !')
    print('This is command line interface of TagCounter')
    print('For gui version enter command start --gui')
    print('For cli version specify site url --url')









