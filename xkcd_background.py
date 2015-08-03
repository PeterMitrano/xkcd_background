import os
import json
import urllib2

json_file = urllib2.urlopen('http://xkcd.com/info.0.json')
file_contents = json_file.read()
as_json = json.loads(file_contents)
img_uri = as_json['img']
cmd = "gsettings gnome.org.desktop.background picture-uri " + img_uri
print "running", cmd
subprocess.call(cmd)
