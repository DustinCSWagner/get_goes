# NOAA GOES Full Disk Live Wallpaper

Let this simple python3 script change your wallpaper to the most recent [NOAA GOES](https://en.wikipedia.org/wiki/Geostationary_Operational_Environmental_Satellite) full disk image. 

Tested and developed on Fedora 27, GNOME 3.26.

*Disclaimer*: this extension is unofficial and not affiliated with NOAA in any way.

## Install

Place the get_goes.py file in its own directory somewhere and run it.
'''
./get_goes.py
'''
This should set your defualt background color to black, download the most recent NOAA GOES jpg, and set it as your Gnome Wallpaper.

If you would like to run this file on a schedule, you can add it to your crontab.

Place the 'add_goes_cron.sh' in the same directory as 'get_goes.py'. Modify the script to reflect the directory you keep the 'get_goes.py' in and run it.
'''
./add_goes_cron.sh
'''
## Testing

You can help with development by testing and reporting issues.  

## Screenshots

