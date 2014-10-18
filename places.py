'''
Copyright(c) 2014 YSUV - This script takes the name of a palce as input and
then plots all teh places in the world that has that name on a map using teh
google maps API.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to
do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from urllib import urlopen
from flask import Flask, request, render_template

import argparse
import json

urlTemplate = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s'
mapurlTemplate = ('https://maps.googleapis.com/maps/api/staticmap?'
                  'center=51.5073509,-0.1277583'
                  '&zoom=1&size=400x400&maptype=hybrid'
                  '&markers=color:blue%7Clabel:S')


def fetchplaceInfoUrl(name):
    ''' This function returns a URL that marks places using
    latitues/longitutes'''
    url = urlTemplate % name
    urlObj = urlopen(url)
    data = urlObj.read()
    placeData = json.loads(data)
    if placeData['status'].lower() == 'ZERO_RESULTS':
        return 0, ''

    results = placeData['results']
    latLong = ''
    for result in results:
        latLong += ('%7C' +
                    str(result['geometry']['location']['lat']) + ',' +
                    str(result['geometry']['location']['lng']) + '%7C')

    url = mapurlTemplate + latLong
    return len(results), url


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/<place>', methods = ['GET'])
def show_entries(place):
    num, url = fetchplaceInfoUrl(place)
    return render_template('map.html', num=num, place=place, url=url)

if __name__ == '__main__':
    app.run()
