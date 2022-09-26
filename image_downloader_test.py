import modules.download_handler as download_handler



full_path = download_handler.build_full_path('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', './content/images', '.png', 'common_yarrow', '14')
print(download_handler.inat_image_downloader('https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png', full_path ))


