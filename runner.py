import sys
import argparse


def greetings():
    print('Super Hi %username% !')
    print('This is command line interface of TagCounter')
    print('For gui version enter command start --gui')
    print('For cli version specify site url --url')


def initializer():
    print(sys.argv)
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser('SUPER HI')
    parser.add_argument('-g', '--get',  help='url to web site page to parse')
    parser.add_argument('-v', '--view', help='url to web site page to parse')
    args = parser.parse_args()

    if args.get:
        print(args.get)
    if args.view:
        print(args.view)
    else:
        print('Loading GUI')






