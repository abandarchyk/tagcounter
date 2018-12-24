import argparse
import GUI
import CLI


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









