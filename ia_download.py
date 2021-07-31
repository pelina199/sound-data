#Download files from archive.org

from internetarchive import download
from internetarchive import get_item

#archive.org id list
# e.g. https://archive.org/download/aporee_2104_20093/berlinBuerkner9BackyardBird020413.ogg
file = 'download-links-koln2.txt'
#save location
filePath = 'E:\\Recordings\\'

with open(file, "r") as file:
    for line in file: 
        words = line.split("/")
        iaID = words[-2]
        item = get_item(iaID)
        #download files smaller than 10 MB
        if item.item_size < 10000000:
            #archive.org API: https://archive.org/services/docs/api/internetarchive/api.html?highlight=download#internetarchive.download
           download(iaID, glob_pattern=['*ogg','*png','*txt'], destdir= filePath, ignore_errors=True, ignore_existing=True)

