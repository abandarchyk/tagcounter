import argparse
from tagcounter import GUI
from tagcounter import CLI


# init parser
parser = argparse.ArgumentParser(usage='Commands: parsing: --get(-g) "website", viewing results: --view(-v) "website"')
parser.add_argument('-g', '--get',  help='url to web site page to parse')
parser.add_argument('-v', '--view', help='url to web site page to parse')
#


def main():
    args = parser.parse_args()
    if args.get or args.view:
        CLI.run(args)
    else:
        GUI.run()


if __name__ == '__main__':
    main()










