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
    bigest_bar = max(bars,
                     key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return bigest_bar


def get_smallest_bar(all_bars):
    smallest_bar = min(bars,
                       key=lambda x: x['properties']['Attributes']['SeatsCount'])
    return smallest_bar

bars = file_connection()

def get_closest_bar(bars, latitude, longitude):
    print(min(bars, key=lambda x: round(vincenty(
        (latitude, longitude), x['geometry']['coordinates']).km, 3)))

get_closest_bar(bars,37.585757, 55.778435)

def get_closest_bar(data, latitude, longitude):
    return min(data, key=lambda data: get_distance(latitude, longitude, data['geoData']['coordinates']))


def get_distance(x1, y1, point):
    return sqrt((x1 - point[0])**2 + (y1 - point[1])**2)

def get_closest_bar(aa, bb):
    for each_bar in bars:
        bar_and_coord = [each_bar['properties']['Attributes']['Name'],each_bar['geometry']['coordinates'][1],each_bar['geometry']['coordinates'][0]]
        distance = vincenty((bar_and_coord[1], bar_and_coord[2]),(aa,bb)).kilometers
        print(bar_and_coord, distance)

    closest_bar = [min(final_list, key=lambda x: x[1])]
    print(closest_bar[0][0])


#git_distnace(bars, 55.778435, 37.585757)

#get_closest_bar(55.778435, 37.585757)

#
# if __name__ == '__main__':
#     bars = file_connection()
#     print('Smalles bar in Moscow: {}'
#           .format(get_smallest_bar(bars)['properties']['Attributes']['Name']))
#     print('Biggest bar in Moscow: {}'
#           .format(get_biggest_bar(bars)['properties']['Attributes']['Name']))
#     try:
#         my_longitude = float(input('To find closest bar enter Longitude: '))
#         my_latitude = float(input('and Latitude: '))
#     except:
#         print('Please, use only digits as Longitude and Latitude')
#         sys.exit(0)
#     print('Closest bar in Moscow: {}'.format(get_closest_bar(bars,
#                                                              my_longitude,
#                                                              my_latitude)))
