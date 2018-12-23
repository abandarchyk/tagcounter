import sys
import argparse
import logging
import results_processor
import tagcounter_config
import GUI
import CLI

# init logger
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


# init parser
parser = argparse.ArgumentParser(usage='Commands: parsing: --get(-g) "website", viewing results: --view(-v) "website"')
parser.add_argument('-g', '--get',  help='url to web site page to parse')
parser.add_argument('-v', '--view', help='url to web site page to parse')
#


if __name__ == '__main__':
    args = parser.parse_args()
    if args.get or args.view:
        CLI.run(args)
    else:
        GUI.run()









