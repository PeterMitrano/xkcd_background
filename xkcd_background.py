import subprocess
import json
import urllib2

json_file = urllib2.urlopen('http://xkcd.com/info.0.json')
file_contents = json_file.read()
as_json = json.loads(file_contents)
img_url = str(as_json['img'])
download = ["wget", img_url, "-O", "/home/peter/.wallpaper.png"]
subprocess.call(download)
cmd = ["gsettings","set" , "org.gnome.desktop.background",  "picture-uri", "file:///home/peter/.wallpaper.png"]
subprocess.call(cmd)
