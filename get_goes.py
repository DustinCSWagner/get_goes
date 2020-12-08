#!/usr/bin/python3
#version no quit

import struct, ctypes, json, os, urllib.request, sys, subprocess
from gi.repository import Gio

#windows helper functions
#set windows wallpaper
#https://stackoverflow.com/questions/1977694/how-can-i-change-my-desktop-background-with-python#1977831
def is_64_windows():
    """Find out how many bits is OS. """
    return struct.calcsize('P') * 8 == 64

def get_sys_parameters_info():
    """Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function. """
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA


#set download resolution
image_size = {"huge":"10848x10848",
              "large":"5424x5424",
              "normal":"1808x1808",
              "small":"678x678",
              "tiny":"339x339"}
resolution = image_size["normal"]

#set current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

filename = "latest.jpg"
remote_file = "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/FD/GEOCOLOR/"+filename
local_file = os.path.join(current_dir,filename)

#retrieve image
try:
    #print('skipping new image')
    urllib.request.urlretrieve(remote_file, local_file)
except:
    print("ERROR: unable to download jpg")
    quit()
    
#check for desktop enviroment type
platform=sys.platform
print("platform=", platform)
if platform=="win32": #for windows
    try:
        #https://msdn.microsoft.com/en-us/library/windows/desktop/ms724947(v=vs.85).aspx
        SPI_SETDESKWALLPAPER = 0x14 
        SPIF_UPDATEINIFILE = 0x01
        SPIF_SENDCHANGE = 0x02;
        #cant find a way to set default background color to black, or to have image
        # 'fit' to desktop. Do that manually, images will still update if scheduled.
        sys_parameters_info = get_sys_parameters_info()
        r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, local_file, SPIF_SENDCHANGE)
    except:
        print("INFO: You can manually set your wallpaper to %s" % local_file)  
elif platform=="darwin": #for mac
    try:
        from appscript import app, mactypes
        app('Finder').desktop_picture.set(mactypes.File(local_file))
    except:
        print("INFO: You can manually set your wallpaper to %s" % local_file)  
else: #for linux/bsd/...
    #https://stackoverflow.com/questions/1977694/how-can-i-change-my-desktop-background-with-python
    desktop_session = os.environ.get("DESKTOP_SESSION")
    print("desktop_session=", desktop_session)
    if desktop_session is not None: 
        desktop_session = desktop_session.lower()         
        if desktop_session=="gnome" or desktop_session=="cinnamon":            
            #set image as background
            try:
                settings = Gio.Settings.new("org.gnome.desktop.background")
                settings.set_string("picture-uri", "file://"+local_file)
                settings.set_string("picture-options", "scaled") #zoom|centered|none|scaled|spanned|stretched|wallpaper
                settings.set_string("primary-color", "#000000") #set background color to black
            except:
                args = ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", "file://"+local_file]
                subprocess.Popen(args)
        elif desktop_session=="lxde":
            args = "pcmanfm --set-wallpaper %s --wallpaper-mode=fit" % local_file
            subprocess.Popen(args,shell=True)
        elif desktop_session=="mate":
            try: # MATE >= 1.6
                #info from http://wiki.mate-desktop.org/docs:gsettings
                args0 = ["gsettings", "set", "org.mate.background", "picture-filename", "'%s'" % local_file]
                args1 = ["gsettings", "set", "org.mate.background", "picture-options", "'scaled'"]
                args2 = ["gsettings", "set", "org.mate.background", "primary-color", "'#000000'"]
                args3 = ["gsettings", "set", "org.mate.background", "color-shading-type", "'solid'"]
                subprocess.Popen(args0)
                subprocess.Popen(args1)
                subprocess.Popen(args2)
                subprocess.Popen(args3)
            except: # MATE < 1.6
                #From https://bugs.launchpad.net/variety/+bug/1033918
                args = ["mateconftool-2","-t","string","--set","/desktop/mate/background/picture_filename",'"%s"' % local_file]
                subprocess.Popen(args) 
        elif desktop_session=="openbox":
            try:
                args = ["feh", "--bg-max", local_file]
                subprocess.Popen(args)
            except:
                print("ERROR: Failed to set wallpaper with feh!\n")
                print("INFO: Please make sure that you have feh installed.\n")
        else:
            print("ERROR: Unsupported linux/bsd desktop enviroment")  
            print("INFO: You can manually to set Your wallpaper to %s" % local_file)
    else:
        #fail back to gnome becuase thats what I use ;)
        try:
            settings = Gio.Settings.new("org.gnome.desktop.background")
            settings.set_string("picture-uri", "file://"+local_file)
            settings.set_string("picture-options", "scaled") #zoom|centered|none|scaled|spanned|stretched|wallpaper
            settings.set_string("primary-color", "#000000") #set background color to black
        except:
            args = ["gsettings", "set", "org.gnome.desktop.background", "picture-uri", "file://"+local_file]
            subprocess.Popen(args)

    
