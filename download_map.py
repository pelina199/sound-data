#Download map image of sound recording location into its respective folder

import math
import re
from pathlib import Path
import urllib.request


def getLocation(txtPath):
    with open(txtPath, "r") as f:
        for line in f:
            if line.find("latitude=") != -1:
                latResult = re.search('latitude=(.*?);', line)
                lat = latResult.group(1)
                
                lonResult = re.search('longitude=(.*?);', line)
                lon = lonResult.group(1)
                
    return lat, lon


def deg2num(lat_deg, lon_deg, zoom):
  lat_rad = math.radians(lat_deg)
  n = 2.0 ** zoom
  xtile = int((lon_deg + 180.0) / 360.0 * n)
  ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
  return xtile, ytile  


def getOsmUrl(lat_deg, lon_deg, zoom):
    smurl = r"http://a.tile.openstreetmap.org/{0}/{1}/{2}.png"
    x, y = deg2num(lat_deg, lon_deg, zoom)
    img_url = smurl.format(zoom, x, y) 
    
    return img_url


def getGoogleUrl(latitude, longitude, zoom, img_size, key):
    smurl = r"https://maps.googleapis.com/maps/api/staticmap?center={0},{1}&zoom={2}&size={3}&key={4}&style=feature:all|element:labels|visibility:off" 
    img_url = smurl.format(latitude, longitude, zoom, img_size, key) 
    
    return img_url


def saveImage(img_url, folderPath):
    parts = folderPath.rsplit("\\", 1)
    saveLocation = parts[0]
    img_name = parts[1].split(".")[0] + "_map.png"

    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    
    urllib.request.urlretrieve(img_url, saveLocation + "\\" + img_name)


filePath = "E:\\Recordings2\\"
paths = Path(filePath).glob('**/*.txt')

zoom_osm = 16
zoom_google = 17
size = "400x400"
#Enter your API key
#api_key = ""

for path in paths:
    lat, lon = getLocation(path)
    #url_osm = getOsmUrl(float(lat), float(lon), zoom_osm)
    url_google = getGoogleUrl(float(lat), float(lon), zoom_google, size, api_key)
    saveImage(url_google, str(path))
