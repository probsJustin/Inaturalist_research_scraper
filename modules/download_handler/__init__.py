import requests
import shutil
import math
import time
import hashlib
import json

def Average(lst):
    return sum(lst) / len(lst)

def url_download_image(url, contentDirectory):
    times = list()
    start = (time.time())
    fileName = hashlib.md5(url.encode('utf-8'))
    fileNameHash = f'inat_{fileName.hexdigest()}.jpg'
    filePath = f'./content/images/inat_{fileName.hexdigest()}.jpg'
    if fileNameHash not in contentDirectory:
        response = requests.get(url, stream=True)
        with open(filePath, 'wb+') as out_file:
            shutil.copyfileobj(response.raw, out_file)
    end = (time.time())
    times.append(end - start)
    print(f'Average Time in Seconds: {Average(times)}')

# Example:
#with open('./content/links/link_page.json') as json_file:
#    data = json.load(json_file)
#contentDirectory = './content/images'
#
#for url in data:
#    url_download_image(url, contentDirectory)