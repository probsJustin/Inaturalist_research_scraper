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

def get_dict_paged_identifications(param_taxon_id, number_of_needed_pages, per_page_param):
    pagedResponse = dict()
    for x in range(1, number_of_needed_pages):
        try:
            pagedResponse[x] = get_identifications(taxon_id=[param_taxon_id], per_page=per_page_param, page=x)
        except Exception as error:
            print(error)
            break
    return pagedResponse

def get_dict_paged_observations(param_taxon_id, number_of_needed_pages, per_page_param):
    pagedResponse = dict()
    for x in range(1, number_of_needed_pages):
        try:
            pagedResponse[x] = get_observations(taxon_id=[param_taxon_id], per_page_param=200, page=x)
        except Exception as error:
            print(error)
            break
    return pagedResponse

def get_image_url(param_inat_response_payload, match_string):
    matches = re.findall(match_string, str(param_inat_response_payload), re.DOTALL)
    return matches

def get_formatted_taxa(taxa_name):
    return get_taxa(q=taxa_name)

def get_taxa_by_name(taxa_name):
    return get_taxa_by_id(q=taxa_name)

def write_content_to_files(responseToWrite, base_name, taxon, page):
    with open(f'./content/requests/{base_name}_{taxon}_{page}.json', "w") as outfile:
        outfile.write(json.dumps(responseToWrite, indent=4, sort_keys=True, default=str))


class result_return_for_image:
    geoLocation = ''
    observationPhoto = ''
    def __init__(self, geoLocation, observationPhoto):
        self.geoLocation = geoLocation
        self.observationPhoto = observationPhoto

    def print(self):
        print(f'GeoLocation: {self.geoLocation}')
        print(f'ObservationPhoto: {self.observationPhoto}')

def process_inat_result_data(data):
    return_list = list()
    for x in data['results']:
        geoLocationLatLong = x['observation']['location']
        observationPhoto = x['observation']['observation_photos'][0]['photo']['url'].replace('square', 'original')
        return_list.append(result_return_for_image(geoLocationLatLong, observationPhoto))
    return return_list