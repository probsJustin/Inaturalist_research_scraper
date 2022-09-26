import modules.download_handler as download_handler
import modules.image_handler as image_handler


image_original_full_path = download_handler.build_full_path('https://inaturalist-open-data.s3.amazonaws.com/photos/2071495/original.JPG', './content/images', '.png', 'common_yarrow', '14')
image_destination_full_path = image_handler.build_destination_image_file_name(image_original_full_path)
download_handler.inat_image_downloader('https://inaturalist-open-data.s3.amazonaws.com/photos/2071495/original.JPG', image_original_full_path )
image_handler.write_to_image_v2(image_original_full_path, image_destination_full_path, 'testing')

