#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import urllib
import sys
from geopy.distance import vincenty
import requests


def load_file():
    path = 'https://devman.org/media/filer_public/95/74/' \
        '957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json'
    url = urllib.request.urlopen(path)
    full_list_of_bars = json.loads(url.read().decode('utf-8'))
    return full_list_of_bars['features']


def get_biggest_bar(all_bars):
    big = max(bars,
              key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return big


def get_smallest_bar(all_bars):
    small = min(bars,
                key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return small


def get_closest_bar(data, my_latitude, my_longitude):
    final_list = []
    for each_bar in bars:
        name = str(each_bar['properties']['Attributes']['Name'])
        coord_1 = str(each_bar['geometry']['coordinates'][1])
        coord_2 = str(each_bar['geometry']['coordinates'][0])
        final_list.append([[name, coord_1, coord_2][0],
                           (vincenty(([name, coord_1, coord_2][2],
                                      [name, coord_1, coord_2][1]),
                                     (my_latitude, my_longitude)).kilometers)])

    closest_bar = [min(final_list, key=lambda x: x[1])]
    return closest_bar[0][0]


if __name__ == '__main__':
    bars = load_file()
    my_longitude = float(input('Enter Longitude: '))
    my_latitude = float(input('Enter Latitude: '))
    print('Closest bar: {}'.format(get_closest_bar(bars,
                                                   my_longitude,
                                                   my_latitude)))
    print('Smalles bar: {}'
          .format(get_smallest_bar(bars)['properties']['Attributes']['Name']))
    print('Biggest bar: {}'
          .format(get_biggest_bar(bars)['properties']['Attributes']['Name']))
