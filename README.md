# NOAA GOES Full Disk Live Wallpaper

Let this simple python3 script change your wallpaper to the most recent [NOAA GOES](https://en.wikipedia.org/wiki/Geostationary_Operational_Environmental_Satellite) full disk image. 
Tested and developed on Fedora 27.
Inspired by Elinvention's [gnome-shell-extension-nasa-apod](https://github.com/Elinvention/gnome-shell-extension-nasa-apod/blob/master/README.md)

*Disclaimer*: this script is unofficial and not affiliated with NOAA in any way.

Supports:
* Windows
* Mac
* Linux
  * Gnome
  * Cinnamon
  * Mate
  * Openbox
  * LXDE

Run once to get the most recent image or on a schedule to update your wallpaper through the day. 

## Install

Place the get_goes.py file in its own directory somewhere and run it.
`./get_goes.py`
This should set your defualt background color to black, download the most recent NOAA GOES jpg, and set it as your Wallpaper.

If you would like to run this file on a schedule, you can add it to your crontab or use window's SCHTASKS.

Place the 'add_goes_cron.sh' or 'schedule_get_goes_windows.bat' in the same directory as 'get_goes.py'. Modify the script to reflect the directory you keep the 'get_goes.py' in and execute the script.
`./add_goes_cron.sh` for mac/linux or `schedule_get_goes_windows.bat` for windows.
## Testing

You can help with development by testing and reporting issues.  I've tested as best I can but there are a lot of possible configurations. 

## Screenshots

![Early evening on GNOME][screenshot1]
![Middayon Windows][screenshot2]

[screenshot1]: https://raw.githubusercontent.com/DustinCSWagner/get_goes/master/screenshots/gnome.png
[screenshot2]: https://raw.githubusercontent.com/DustinCSWagner/get_goes/master/screenshots/windows.png
