import os

from PIL import Image, ImageDraw, ImageFont
from geopy.geocoders import Nominatim

example_imageLocation = './content/images/original_1.jpg'
example_imageDestinationLocation = './content/images/original_2.jpg'
example_lat_long_example = "53.0483695,-9.1397471667"
example_name = 'common yarrow'
example_taxon = 52818
example_date_of_image = f'5/15/2022'

height = 1255
width = 2500

size = dict()
size['height'] = 1255
size['width'] = 2500

FONT_LOCATION = './content/fonts/Mogen-Bold.ttf'

def determine_location(lat_long_string):
    geolocator = Nominatim(user_agent="geoapiExercises")
    geoLocation = geolocator.reverse(lat_long_string)
    geoLocation = str(geoLocation)
    geoLocation = geoLocation.split(', ')
    geoLocation = ', '.join(geoLocation[:int(len(geoLocation)/2)]) + ' \n ' + ', '.join(geoLocation[int(len(geoLocation)/2):])
    return geoLocation

def get_file_name_without_suffix(file_name):
    return os.path.splitext(file_name)[0]

def get_file_suffix(file_name)
    return os.path.splitext(file_name)[1]

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
        print(f'Found File: {file_path}')
        return True
    else:
        print(f'Not able to find file: {file_path}')
        return False

def write_to_image(image_location, image_destination, text_to_write, size, debug = None):
    rectangle_size = determine_rectangle_size(size)
    text_size = determine_text_size(size)
    position = determine_position(size)
    text_position = determine_text_position(size)

    img = Image.open(image_location)
    d1 = ImageDraw.Draw(img)
    d1.rectangle((rectangle_size, position), fill="white")
    d1.text(text_position, text_to_write, font=ImageFont.truetype(FONT_LOCATION, text_size), fill=(0, 0, 0))
    if(debug == 'show'):
        img.show()
    img.save(image_destination)

def build_destination_image_file_name(original_image):
    destination_image_file_name_ext = os.path.splitext(original_image)[0]
    return f'{original_image}_image_processed.{destination_image_file_name_ext}'


def write_to_image_v2(original_location, destination_location,  text_to_write, debug = None):

    if(does_file_exist(original_location)):
        if(does_file_exist(destination_location)):
            return True
        else:
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
        print(f'The input for the image writer does not appear to be available.')
        return False


#image_text = built_image_text(determine_location(example_lat_long_example), example_taxon, example_name, example_date_of_image)
#write_to_image(example_imageLocation, example_imageDestinationLocation, image_text, size)