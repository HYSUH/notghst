'''
Copyright(c) 2014 YSUV 
MIT licence
'''

from urllib import urlopen
from bs4 import BeautifulSoup
import argparse

url_template = 'https://docs.python.org/%s/library/index.html'
DASH = u'\u2014'


def getPythonModules(version):
    '''
        Given a python version, this function returns a list of modules and
        their corresponding description.
    '''
    url = url_template % version
    urlObj = urlopen(url)
    data = urlObj.read()

    # Get only the text and remove all the html tags
    modulelist = BeautifulSoup(data).text.split('\n')
    results = {}
    for module in modulelist:
        # 20.1. webbrowser - Convenient Web-browser controller
        result = module.split(DASH)
        if len(result) != 2:
            continue

        module, desc = result

        # 20.1. webbrowser  -> webbrowser
        module = module.split()[1]
        results[module] = desc

    return results


def checkModuleSupported(version, module):
    '''
        Given a python version and a module, this function returns whether the
        module is supproted in that version or nor
    '''
    modules = getPythonModules(version)
    return module in modules


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get the list of '
                                                 'python modules '
                                                 'based on version')

    parser.add_argument('version', help='python version')
    parser.add_argument('module', nargs='?', help='module to check')
    args = parser.parse_args()
    if args.module:
        if checkModuleSupported(args.version, args.module):
            print args.module + ' is supported'
        else:
            print args.module + ' is not supported'
    else:
        print getPythonModules(args.version).keys()
