#!/usr/bin/python


import json
import urllib
import sys
from geopy.distance import vincenty
import requests


def file_connection():
    path = ('https://devman.org/media/filer_public/95/74/'
            '957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json')
    url = urllib.request.urlopen(path)
    full_list_of_bars = json.loads(url.read().decode('utf-8'))
    return full_list_of_bars['features']


def get_biggest_bar(all_bars):
    biggest_bar = max(bars,
                     key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return biggest_bar


def get_smallest_bar(all_bars):
    smallest_bar = min(bars,
                       key=lambda x:
                       x['properties']['Attributes']['SeatsCount'])
    return smallest_bar


def get_closest_bar(bars, latitude, longitude):
    closest_bar_info = min(bars, key=lambda x: round(vincenty(
        (latitude, longitude), x['geometry']['coordinates']).kilometers, 3))
    return closest_bar_info['properties']['Attributes']['Name']

if __name__ == '__main__':
    bars = file_connection()
    print('Smalles bar in Moscow: {}'
          .format(get_smallest_bar(bars)['properties']['Attributes']['Name']))
    print('Biggest bar in Moscow: {}'
          .format(get_biggest_bar(bars)['properties']['Attributes']['Name']))
    try:
        my_longitude = float(input('To find closest bar enter Longitude: '))
        my_latitude = float(input('and Latitude: '))
    except:
        print('Please, use only digits as Longitude and Latitude')
        sys.exit(0)
    print('Closest bar in Moscow: {}'.format(get_closest_bar(bars,
                                                             my_longitude,
                                                             my_latitude)))
