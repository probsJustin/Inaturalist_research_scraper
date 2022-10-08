import os

from PIL import Image, ImageDraw, ImageFont
from geopy.geocoders import Nominatim
import modules.internal_logger as logger



height = 1255
width = 2500

size = dict()
size['height'] = 1255
size['width'] = 2500

#FONT_LOCATION = './content/fonts/Mogen-Bold.ttf'
FONT_LOCATION = './content/fonts/PocketMonk-15ze.ttf'

def determine_location(lat_long_string):
    geolocator = Nominatim(user_agent="geoapiExercises")
    geoLocation = geolocator.reverse(lat_long_string)
    geoLocation = str(geoLocation)
    geoLocation = geoLocation.split(', ')
    geoLocation = ', '.join(geoLocation[:int(len(geoLocation)/2)]) + ' \n ' + ', '.join(geoLocation[int(len(geoLocation)/2):])
    return geoLocation

def get_file_name_without_suffix(file_name):
    return os.path.splitext(file_name)[0]

def get_file_name_ext(file_name):
    return os.path.splitext(file_name)[1]

def get_file_basename(file_name):
    return os.path.basename(file_name)

def determine_text_size(size):
    return 40


def determine_rectangle_size(size):
    return (width, 300)


def determine_text_position(size):
    return (0, 100)


def determine_position(size):
    return (0, 100)


def built_image_text(location, taxon, name, date_of_image):
    return f' LOCATION: {location} \n TAXON: {taxon} \n NAME: {name} \n DATE: {date_of_image}'

def does_file_exist(file_path):
    if(os.path.exists(file_path)):
        logger.log_this('image_handler', f'Found File: {file_path}')
        return True
    else:
        logger.log_this('image_handler', f'Not able to find file: {file_path}')
        return False


def build_destination_image_file_name(original_image):
    destination_image_file_name_ext = get_file_name_ext(original_image)
    basename_original_image = get_file_name_without_suffix(original_image)
    return f'{basename_original_image}_image_processed{destination_image_file_name_ext}'


def write_to_image_v2(original_location, destination_location,  text_to_write, debug = None):
    logger.log_this('image_handler', f'Perparing to write to image {destination_location}')
    if(does_file_exist(original_location)):
        if(does_file_exist(destination_location)):
            logger.log_this('image_handler', f'Skipping image processesing for image: {destination_location} \n ...')
            return True
        else:
            logger.log_this('image_handler', f'Writing to image: {destination_location} \n ...')
            rectangle_size = determine_rectangle_size(size)
            text_size = determine_text_size(size)
            position = determine_position(size)
            text_position = determine_text_position(size)

            img = Image.open(original_location)
            d1 = ImageDraw.Draw(img)
            d1.rectangle((rectangle_size, position), fill="white")
            d1.text(text_position, text_to_write, font=ImageFont.truetype(FONT_LOCATION, text_size), fill=(0, 0, 0))
            if (debug == 'show'):
                img.show()
            img.save(destination_location)
            return True
    else:
        logger.log_this('image_handler', f'The input for the image writer does not appear to be available.')
        return False

def write_to_bottom_of_image(original_location, destination_location,  text_to_write, debug = None):
    logger.log_this('image_handler', f'Perparing to write to image {destination_location}')
    if(does_file_exist(original_location)):
        if(does_file_exist(destination_location)):
            logger.log_this('image_handler', f'Skipping image processesing for image: {destination_location} \n ...')
            return True
        else:
            logger.log_this('image_handler', f'Writing to image: {destination_location} \n ...')
            rectangle_size = determine_rectangle_size(size)
            text_size = determine_text_size(size)
            position = determine_position(size)
            text_position = determine_text_position(size)

            img = Image.open(original_location)
            bottom_band = Image.new('RGB', (img.size[0], img.size[1] + 200))
            bottom_band.paste(img, (0, 0))
            d1 = ImageDraw.Draw(bottom_band)
            d1.rectangle(((0, img.size[1]), (img.size[0], img.size[1] + 200)), fill="white")
            d1.text((0, img.size[1]), text_to_write, font=ImageFont.truetype(FONT_LOCATION, text_size), fill=(0, 0, 0))
            if (debug == 'show'):
                bottom_band.show()
            bottom_band.save(destination_location)
            return True
    else:
        logger.log_this('image_handler', f'The input for the image writer does not appear to be available.')
        return False
