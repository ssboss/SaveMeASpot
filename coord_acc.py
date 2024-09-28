# code to get coords from the user for the lot

import requests
from selenium import webdriver
import folium
import datetime
import time

def coord_getter(): # general coord getter fxn that pulls from this website
    try:
        data_collection = requests.get('https://ipinfo.io')
        data = data_collection.json()
        location = data['loc'].split(',')
        lat, long = float(location[0]), float(location[1])
        coords = (lat, long)
        return coords
    except:
        error_codes = [400, 401, 403, 404, 405, 408, 500, 501, 502, 503, 504, 301, 302, 304]
        if data_collection.status_code() in error_codes:
            print("An error occurred when procuring the data.\n")
            exit()
            return False

# include the fxn in other files w/ import