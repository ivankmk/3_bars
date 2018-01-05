#!/usr/bin/python


import json
import sys
from geopy.distance import vincenty


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_reader:
        return json.load(file_reader)


def get_biggest_bar(all_bars):
    biggest_bar = max(bars, key=lambda x: x['SeatsCount'])
    return biggest_bar


def get_smallest_bar(all_bars):
    smallest_bar = min(bars, key=lambda x: x['SeatsCount'])
    return smallest_bar


def get_closest_bar_name(bars, latitude, longitude):
    closest_bar_info = min(bars, key=lambda x: round(vincenty(
        (latitude, longitude), x['geoData']['coordinates']).kilometers, 3))
    return closest_bar_info['Name']

if __name__ == '__main__':
    try:
        bars = load_data(input('Please enter path to JSON file with Bars: '))
    except FileNotFoundError:
        sys.exit('Please, use correct filepath')
    print('Smalles bar in Moscow: {}'
          .format(get_smallest_bar(bars)['Name']))
    print('Biggest bar in Moscow: {}'
          .format(get_biggest_bar(bars)['Name']))
    try:
        my_longitude = float(input('To find closest bar enter Longitude: '))
        my_latitude = float(input('and Latitude: '))
    except ValueError:
        sys.exit('Please, use only digits as Longitude and Latitude')
    print('Closest bar in Moscow: {}'.format(
            get_closest_bar_name(bars, my_longitude, my_latitude)
            )
          )
