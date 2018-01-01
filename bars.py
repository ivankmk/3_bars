
import json
import urllib
import sys
from geopy.distance import vincenty
import requests


def load_file():
    url_address = "https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json"
    url = urllib.request.urlopen(url_address)
    list_with_dict = json.loads(url.read().decode("utf-8"))
    return(list_with_dict["features"])

def get_biggest_bar():
    my_max = max(d['properties']['Attributes']['SeatsCount'] for d in load_file())
    max_sits_place = max(load_file(), key=lambda x:x['properties']['Attributes']['SeatsCount'])
    return(str(max_sits_place['properties']['Attributes']["Name"]))

def get_smallest_bar():
    my_min = min(d['properties']['Attributes']['SeatsCount'] for d in load_file())
    min_sits_place = min(load_file(), key=lambda x:x['properties']['Attributes']['SeatsCount'])
    return(str(min_sits_place['properties']['Attributes']["Name"]))

def get_closest_bar():
    my_location=(my_latitude,my_longitude)
    final_list=[]
    for each_line_of_bar in load_file():
        final_list_3=[str(each_line_of_bar['properties']['Attributes']['Name']), str(each_line_of_bar["geometry"]["coordinates"][1]), str(each_line_of_bar["geometry"]["coordinates"][0])]
        final_list_2=[final_list_3[0], (vincenty((final_list_3[2],final_list_3[1]),my_location).kilometers)]
        final_list.append(final_list_2)

    bar = [min(final_list, key=lambda x: x[1])]
    print('Your closest bar is:  {}'.format(str(bar[0][0])))

if __name__ == '__main__':
    my_longitude=float(input("Enter Longitude: "))
    my_latitude=float(input("Enter Latitude: "))

get_closest_bar()
