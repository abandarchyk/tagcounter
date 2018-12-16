import sys
import argparse
import logging


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

print()


def greetings():
    print('Super Hi %username% !')
    print('This is command line interface of TagCounter')
    print('For gui version enter command start --gui')
    print('For cli version specify site url --url')


def initializer():
    print(sys.argv)
#    parser = argparse.ArgumentParser('SUPER HI')
#    parser.add_argument('-g', '--get',  help='url to web site page to parse')
#    parser.add_argument('-v', '--view', help='url to web site page to parse')
#    args = parser.parse_args()

#    if args.get:
#        print(args.get)
#    if args.view:
#        print(args.view)
#    else:
#        print('Loading GUI')






