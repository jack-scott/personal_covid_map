import sys
import requests
import os 
from datetime import date, datetime, timedelta

#creates a URL to point to Google location kml file based on requested date
def create_url(_year, _month, _day):
    year = int(_year)
    #month is zero indexed
    month = int(_month) - 1
    day = int(_day)
    url_str = "https://www.google.com/maps/timeline/kml?authuser=0&pb=%211m8%211m3%211i{}%212i{}%213i{}%212m3%211i{}\
%212i{}%213i{}".format(year, month, day, year, month -2, day)
    return url_str

#gets and saves results from a given URL 
def download_and_save(url, filename, save_folder, filetype=".kml"):
    result = requests.get(url, allow_redirects=True)
    #prepend "." to filetype if not present
    if filetype[0] is not ".":
        filetype = ".{}".format(filetype)
    outfile = "{}{}".format(filename, filetype)
    curr_path = os.path.dirname(os.path.abspath(__file__))
    outpath = os.path.join(curr_path, save_folder, outfile)
    open(outpath, 'wb').write(result.content)

#collects X number of previous days location data
def get_past_days_location(num_days):
    for i in range(0, num_days):
        date = datetime.today() - timedelta(days=-i)
        date_str = date.strftime("%d_%m_%Y")
        new_url = create_url(date.year, date.month, date.day)
        print(new_url)
        download_and_save(new_url, date_str, "personal_location")

if __name__ == "__main__":
    get_past_days_location(14)
