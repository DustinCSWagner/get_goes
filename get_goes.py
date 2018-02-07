#!/usr/bin/python3

from gi.repository import Gio
import json, os, urllib.request

#set download resolution
image_size = {"huge":"10848x10848",
              "large":"5424x5424",
              "normal":"1808x1808",
              "small":"678x678",
              "tiny":"339x339"}
resolution = image_size["normal"]

#set current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

#retrive json
goes_json = "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/catalog.json"
local_goes_json = os.path.join(current_dir,"catalog.json")
urllib.request.urlretrieve(goes_json, local_goes_json)

#parse json to get latest image filename
local_json = json.load(open(local_goes_json))
filename = local_json["links"][resolution]["fullname"]

#check if file already exists
#quit now or remove other jpg files so that we only have the one we are about to download
if os.path.isfile(filename):
    quit()
else:
    filelist = [ f for f in os.listdir(current_dir) if f.endswith(".jpg") ]
    for f in filelist:
        os.remove(os.path.join(current_dir, f))

#retrieve image
remote_file = "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/"+filename
local_file = os.path.join(current_dir,filename)
urllib.request.urlretrieve(remote_file, local_file)


#set image as background
settings = Gio.Settings.new("org.gnome.desktop.background")
settings.set_string("picture-uri", "file://"+local_file)
settings.set_string("picture-options", "scaled") #zoom|centered|none|scaled|spanned|stretched|wallpaper
settings.set_string("primary-color", "#000000") #set background color to black
