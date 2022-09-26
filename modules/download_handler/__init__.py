import requests
import shutil
import math
import time
import hashlib
import json
import os


def Average(lst):
    return sum(lst) / len(lst)

def url_download_image(url, contentDirectory):
    times = list()
    start = (time.time())
    fileName = hashlib.md5(url.encode('utf-8'))
    fileNameHash = f'inat_{fileName}.jpg'
    filePath = f'{contentDirectory}/inat_{fileName.hexdigest()}.jpg'
    if fileNameHash not in contentDirectory:
        response = requests.get(url, stream=True)
        with open(filePath, 'wb+') as out_file:
            shutil.copyfileobj(response.raw, out_file)
    end = (time.time())
    times.append(end - start)
    print(f'Average Time in Seconds: {Average(times)}')
    return filePath


def hash_file_name(file_name):
    return (hashlib.md5(file_name.encode('utf-8'))).hexdigest()

def build_file_name(url, file_type,  plant_common_name, inat_id):
    return_object = f'{plant_common_name}_{inat_id}_{hash_file_name(url)}{file_type}'
    print(f'build_file_name: {return_object}')
    return return_object

def does_file_exist(file_path):
    if(os.path.exists(file_path)):
        print(f'Found File: {file_path}')
        return True
    else:
        print(f'Not able to find file: {file_path}')
        return False

def download_image(url, file_path):
    try:
        response = requests.get(url, stream=True)
        with open(file_path, 'wb+') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        return True
    except Exception as error:
        print(f'Not able to download the image, recieved error as: {error}')
        return False

def build_full_path(url, directory, file_type, plant_common_name, inat_id):
    return f'{directory}/{build_file_name(url, file_type, plant_common_name, inat_id)}'

def inat_image_downloader(url, full_path):
    if(does_file_exist(full_path)):
        print(f'Skipping downloading file....')
        return True
    else:
        print(f'image full path is {full_path}')
        return download_image(url, full_path)


# Example:
#with open('./content/links/link_page.json') as json_file:
#    data = json.load(json_file)
#contentDirectory = './content/images'
#
#for url in data:
#    url_download_image(url, contentDirectory)