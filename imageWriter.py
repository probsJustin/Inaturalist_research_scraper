from PIL import Image, ImageDraw, ImageFont
from geopy.geocoders import Nominatim



example_imageLocation = './content/images/original_1.jpg'
example_imageDestinationLocation = './content/images/original_2.jpg'
example_lat_long_example = "53.0483695,-9.1397471667"
example_name = 'common yarrow'
example_taxon = 52818

height = 1255
width = 2500

size = dict()
size['height'] = 1255
size['width'] = 2500

FONT_LOCATION = './content/fonts/Mogen-Bold.ttf'

def determine_location(lat_long_string):
    geolocator = Nominatim(user_agent="geoapiExercises")
    return geolocator.reverse(lat_long_string)


def determine_text_size(size):
    return 40


def determine_rectangle_size(size):
    return (width, 250)


def determine_text_position(size):
    return (0, 100)


def determine_position(size):
    return (0, 100)


def built_image_text(location, taxon, name):
    return f' LOCATION: {location} \n TAXON: {taxon} \n NAME: {name}'


def write_to_image(image_location, image_destination, text_to_write, size):
    rectangle_size = determine_rectangle_size(size)
    text_size = determine_text_size(size)
    position = determine_position(size)
    text_position = determine_text_position(size)

    img = Image.open(image_location)
    d1 = ImageDraw.Draw(img)
    d1.rectangle((rectangle_size, position), fill="white")
    d1.text(text_position, text_to_write, font=ImageFont.truetype(FONT_LOCATION, text_size), fill=(0, 0, 0))
    img.show()
    img.save(image_destination)


image_text = built_image_text(determine_location(example_lat_long_example), example_taxon, example_name)
write_to_image(example_imageLocation, example_imageDestinationLocation, image_text, size)