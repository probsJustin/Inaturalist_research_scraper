import modules.download_handler as download_handler
import modules.image_handler as image_handler


url = 'https://inaturalist-open-data.s3.amazonaws.com/photos/2071495/original.JPG'
directory = './content/images'
image_extension = '.png'
plant_name = 'common_yarrow'
plant_id = '14'

text = 'testing'
image_original_full_path = download_handler.build_full_path(url, directory, image_extension, plant_name, plant_id)
image_destination_full_path = image_handler.build_destination_image_file_name(image_original_full_path)
download_handler.inat_image_downloader(url, image_original_full_path )
image_handler.write_to_bottom_of_image(image_original_full_path, image_destination_full_path, text, 'show')

