### Imports
import re
import time
import altair as alt
import ipyplot
import pandas as pd
import json
from IPython.display import Image
from pyinaturalist import (
    Taxon,
    enable_logging,
    get_taxa,
    get_taxa_autocomplete,
    get_taxa_by_id,
    get_observations,
    get_identifications,
    pprint,
)
import os


import logging as internal_logger
import modules.response_handler as response_handler
import modules.util as util
import modules.image_handler as image_handler
import modules.download_handler as download_handler

from rich import print
import time

### Setup
internal_logger.basicConfig(filename=f'./logs/inat_{time.strftime("%Y%m%d-%H%M%S")}.log', level=internal_logger.DEBUG)
enable_logging()
internal_logger.debug(f'Testing.....')


def get_paged_observations(taxon_id, items_per_page):
    print('get_paged_observations')
    internal_logger.debug(f'Testing.....')
    response = get_identifications(taxon_id=[52818], per_page=5, page=1)
    number_of_pages_needed = response_handler.get_total_pages(response, 5)

    pagedResponse = dict()

    pagedResponse = util.get_dict_paged_identifications(52818, number_of_pages_needed, 5)

    unique = dict()
    for y in pagedResponse:
        #print(f'\nPAGE: {y}\n')
        #pprint(pagedResponse[y])
        util.write_content_to_files(pagedResponse[y], "page_identification", 52818, y)



    response = get_observations(taxon_id=[52818], per_page=5, page=1)
    number_of_pages_needed = response_handler.get_total_pages(response, 5)
    pagedResponse = dict()
    pagedResponse = util.get_dict_paged_observations(52818, number_of_pages_needed, 5)
    return pagedResponse

def get_paged_identifications(taxon_id, items_per_page):
    internal_logger.debug(f'Testing.....')
    response = get_identifications(taxon_id=[taxon_id], per_page=items_per_page, page=1)
    number_of_pages_needed = response_handler.get_total_pages(response, 5)

    pagedResponse = dict()
    pagedResponse = util.get_dict_paged_identifications(52818, number_of_pages_needed, 5)

    paged_imaged_data = list()
    for y in pagedResponse:
        util.write_content_to_files(pagedResponse[y], "page_identification", 52818, y)
        paged_imaged_data = paged_imaged_data + util.process_inat_result_data(pagedResponse[y])

    return paged_imaged_data

unique_common_name = dict()

requestFile = f'./requests.txt'
if(not os.path.exists(requestFile)):
    print(f'You will need to create a request file, that has the links that you want to scrape')
    exit(1)
else:
    taxon_info = ""
    for x in  util.get_requests_from_entry_file(requestFile):
        taxon_id = str(util.get_taxon_id_from_url(x)[1])
        if(not taxon_id.isnumeric()):
            print(f'We were not able to find the taxon id in the request that you provided, recieved: {taxon_id}')
            exit(1)
        taxon_info = get_taxa_by_id(str(util.get_taxon_id_from_url(x)[1]))
        for results in taxon_info['results']:
            for photos in results['taxon_photos']:
                try:
                    unique_common_name[photos['taxon']['preferred_common_name']] = results['id']
                except Exception as error:
                    print(f'Non-issue warning: {error}')

    for common_name in unique_common_name:
        for x in get_paged_identifications(unique_common_name[common_name], 5):

             path = f'./content/images/{common_name}-{unique_common_name[common_name]}'

             if(not os.path.exists(path)):
                 os.makedirs(path)

             image_original_full_path = download_handler.build_full_path(
                 x.observationPhoto,
                 path,
                 download_handler.get_url_ext(x.observationPhoto),
                 unique_common_name[common_name],
                 common_name)
             image_text = image_handler.built_image_text(
                 image_handler.determine_location(x.geoLocation),
                 unique_common_name[common_name],
                 common_name,
                 x.date_time_stamp)
             image_destination_full_path = image_handler.build_destination_image_file_name(image_original_full_path)

             download_handler.inat_image_downloader(
                 x.observationPhoto,
                 image_original_full_path
             )
             image_handler.write_to_image_v2(image_original_full_path, image_destination_full_path, image_text)

