import shutil
import hashlib
import os
import requests
import mimetypes
import modules.internal_logger as logger


def hash_file_name(file_name):
    return (hashlib.md5(file_name.encode('utf-8'))).hexdigest()

def build_file_name(url, file_type,  plant_common_name, inat_id):
    return_object = f'{plant_common_name}_{inat_id}_{hash_file_name(url)}{file_type}'
    logger.log_this('download_handler', f'build_file_name: {return_object}')
    return return_object

def get_url_ext(url):
    response = requests.get(url)
    content_type = response.headers['content-type']
    extension = mimetypes.guess_extension(content_type)
    return_object = f'{extension}'
    return return_object

def does_file_exist(file_path):
    if(os.path.exists(file_path)):
        logger.log_this('download_handler', f'Found File: {file_path}')
        return True
    else:
        logger.log_this('download_handler', f'Not able to find file: {file_path}')
        return False

def download_image(url, file_path):
    try:
        response = requests.get(url, stream=True)
        with open(file_path, 'wb+') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        return True
    except Exception as error:
        logger.log_this('download_handler', f'Not able to download the image, recieved error as: {error}')
        return False

def build_full_path(url, directory, file_type, plant_common_name, inat_id):
    return f'{directory}/{build_file_name(url, file_type, plant_common_name, inat_id)}'

def inat_image_downloader(url, full_path):
    if(does_file_exist(full_path)):
        logger.log_this('download_handler', f'Skipping downloading file....')
        return True
    else:
        logger.log_this('download_handler', f'image full path is {full_path}')
        return download_image(url, full_path)




