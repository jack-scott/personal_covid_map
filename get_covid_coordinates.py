from __future__ import division 
from geopy.geocoders import Nominatim
import simplekml
import json
from bs4 import BeautifulSoup
import requests
import os

#given a location as tring, return the coordinates (assume Australia by default)
def get_coordinates_of_location(location, address, city, country="Australia"):
    geolocator = Nominatim(user_agent="my_user_agent")
    loc = geolocator.geocode(address + ',' + city+','+ country)
    print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)
    return {"name":location, "lat":loc.latitude, "long":loc.longitude}

#create kml file from location list
def create_and_save_kml(loc_array, filename="covid_locations.kml"):
    #create basic kml file with locations
    kml=simplekml.Kml()
    for loc in loc_array:
        kml.newpoint(name=loc["Venue"], coords=[(loc["Lon"],loc["Lat"])])

    #get current working directory
    curr_path = os.path.dirname(os.path.abspath(__file__))
    kml_filename = filename
    kml_save_folder =  "covid_locations"
    kml_save_path = os.path.join(curr_path, kml_save_folder, kml_filename)
    kml.save(kml_save_path)

#collect covid locations from www.data.nsw.gov.au and return JSON
def scrape_covid_locations():
    response = requests.get("https://data.nsw.gov.au/data/dataset/0a52e6c1-bc0b-48af-8b45-d791a6d8e289/resource/f3a28eed-8c2a-437b-8ac1-2dab3cf760f9/download/venue-data.json")
    full_response_json = response.json()
    json_data = full_response_json["data"]
    json_locations = json_data["monitor"]
    return json_locations

if __name__ == "__main__":
    locations = scrape_covid_locations()
    create_and_save_kml(locations)

