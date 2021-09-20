import time

import requests
from datetime import datetime
import requests
from uncertainties import *
import smtplib


my_lat = 52.489201
my_long = -0.679600

# ISS Position  ###########

def iss_visible():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status() # This catches errors
    iss_data = response.json()
    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lon = float(iss_data["iss_position"]["longitude"])
    if ufloat(my_lat, 5) <= iss_lat and ufloat(my_long, 5) <= iss_lon:
        return True



# Current Time


# My Sunrise and Sunset times###
def is_night():
    query = {'lat':'52.496670', 'lon':'-0.727150', 'formatted': 0}
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=query)
    response.raise_for_status() # This catches errors
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    hour = time_now.hour
    if hour >= sunset or hour <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_night() and iss_visible():
        pass # send an email


# time_now = datetime.now()
# hour = time_now.hour
# # print(sunrise)
# # print(sunset)
# print(time_now)
# print(hour)
#
# iss_visible()




