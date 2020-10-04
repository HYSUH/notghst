'''
MIT licence - This script takes the name of a palce as input and
then plots all the places in the world that has that name on a map using the
google maps API.

MIT licence
'''

from urllib import urlopen
from flask import Flask, request, render_template

import argparse
import json


urlTemplate = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s'
mapurlTemplate = 'https://maps.googleapis.com/maps/api/staticmap?%s'
markerTemplate = ('center=0,0'
                  '&zoom=1&size=600x600&maptype=hybrid'
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

    url = mapurlTemplate + markerTemplate + latLong
    return len(results), url


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/<place>', methods = ['GET'])
def show_entries(place):
    num, url = fetchplaceInfoUrl(place)
    return render_template('map.html', num=num, place=place, url=url)

if __name__ == '__main__':
    app.run(debug=True)
