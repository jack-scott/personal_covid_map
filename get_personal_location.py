import sys
import requests
import os
from datetime import date, datetime, timedelta
import webbrowser


# creates a URL to point to Google location kml file based on requested date
def create_url(_year, _month, _day):
    year = int(_year)
    # month is zero indexed
    month = int(_month) - 1
    day = int(_day)
    # url_str = "https://timeline.google.com/maps/timeline/kml?authuser=0&amp;pb=!1m8!1m3!1i{}!2i{}!3i{}!2m3!1i{}!2i{}!3i{}".format(year, month, day, year, month , day)
    url_str = "https://www.google.com/maps/timeline/kml?authuser=0&pb=%211m8%211m3%211i{}%212i{}%213i{}%212m3%211i{}\
%212i{}%213i{}".format(year, month, day, year, month, day)
    return url_str


# gets and saves results from a given URL
def download_and_save(url, filename, save_folder, filetype=".kml"):
    # it appears that you have to open the URL through a browser so that Google can access the right cookies
    # its a little bit dirty since this will spawn and close 14 tabs and put all of the location data in your
    # downloads folder
    # imagine just making it easy Google... like an API or something
    webbrowser.open(url)

    # result = requests.get(url, allow_redirects=False)
    # #prepend "." to filetype if not present
    # if filetype[0] is not ".":
    #     filetype = ".{}".format(filetype)
    # outfile = "{}{}".format(filename, filetype)
    # curr_path = os.path.dirname(os.path.abspath(__file__))
    # outpath = os.path.join(curr_path, save_folder, outfile)
    # open(outpath, 'wb').write(result.content)


# collects X number of previous days location data
def get_past_days_location(num_days):
    for i in range(0, num_days):
        date = datetime.today() - timedelta(days=i)
        date_str = date.strftime("%d_%m_%Y")
        new_url = create_url(date.year, date.month, date.day)
        print(new_url)
        download_and_save(new_url, date_str, "personal_location")


if __name__ == "__main__":
    get_past_days_location(14)
