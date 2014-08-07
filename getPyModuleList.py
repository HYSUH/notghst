'''
Copyright(c) 2014 HYSUH - 

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in the
Software without restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN
AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
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
    url = url_template %version
    urlObj = urlopen(url)
    data = urlObj.read()

    #Get only the text and remove all the html tags
    modulelist = BeautifulSoup(data).text.split('\n')
    results = {}
    for module in modulelist:
        #20.1. webbrowser - Convenient Web-browser controller
        result = module.split(DASH)
        if len(result) != 2:
            continue

        module, desc = result

        #20.1. webbrowser  -> webbrowser
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
    parser = argparse.ArgumentParser(description='Get the list of python'
                        'modules based on version')

    parser.add_argument('version', help='python version')
    args = parser.parse_args()
    print getPythonModules(args.version).keys()
    
    checkModuleSupported('2.7', 'turtle')