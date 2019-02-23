# Dependencies
import requests
import json

# Google developer API key
from config import gkey

# 1. What are the geocoordinates (latitude/longitude) of Seattle, Washington?
target_city = "Seattle, Washington"
target_url = ('https://maps.googleapis.com/maps/api/geocode/json?'
    'address={0}&key={1}').format(target_city, gkey)
geo_data = requests.get(target_url).json()
lat = geo_data["results"][0]["geometry"]["location"]["lat"]
lng = geo_data["results"][0]["geometry"]["location"]["lng"]

# Print the latitude and longitude
print('''
    City: {0}
    Latitude: {1}
    Longitude: {2}
    '''.format(target_city, lat, lng))
    
# 2. What are the geocoordinates (latitude/longitude) of The White House?
target_city = "The White House"
target_url = ('https://maps.googleapis.com/maps/api/geocode/json?'
    'address={0}&key={1}').format(target_city, gkey)
geo_data = requests.get(target_url).json()
lat1 = geo_data["results"][0]["geometry"]["location"]["lat"]
lng1 = geo_data["results"][0]["geometry"]["location"]["lng"]

# Print the latitude and longitude
print('''
    City: {0}
    Latitude: {1}
    Longitude: {2}
    '''.format(target_city, lat1, lng1))
    
# 3. Find the name and address of a bike store in Seattle, Washington.
#    Hint: See https://developers.google.com/places/web-service/supported_types
target_coordinates = str(lat)+", "+str(lng)
target_search = "Bike Store"
target_radius = 8000
target_type = "bicycle_store"

# set up a parameters dictionary
params = {
    "location": target_coordinates,
    "keyword": target_search,
    "radius": target_radius,
    "type": target_type,
    "key": gkey
}

# base url
base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

# run a request using our params dictionary
response = requests.get(base_url, params=params)

places_data = response.json()
print(places_data["results"][0]["name"])
print(places_data["results"][0]["vicinity"])
