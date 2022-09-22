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
    """
        Parameters
        ----------
        param_taxon_id :
            get a specific taxon
        number_of_needed_pages :
            number of pages that you want to attempt to retrieve
        per_page_param :
            how many pages per instance

        Returns
        -------
        returns :
            list of paged responses
    """
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
    date_time_stamp = ''
    def __init__(self, geoLocation, observationPhoto, createAtDate):
        """
            Parameters
            ----------
            geoLocation :  str
                geoLocation of a specific image
            observationPhoto :  str
                url of a specific image
            createAtDate : str
                date of the creation of the post
        """
        self.geoLocation = geoLocation
        self.observationPhoto = observationPhoto
        self.date_time_stamp = createAtDate

    def print(self):
        print(f'GeoLocation: {self.geoLocation}')
        print(f'ObservationPhoto: {self.observationPhoto}')
        print(f'createAtDate: {self.date_time_stamp}')

    def __repr__(self):
        return f'GeoLocation: {self.geoLocation}, ObservationPhoto: {self.observationPhoto}, date: {self.date_time_stamp}'



def process_inat_result_data(data):
    """
        Parameters
        ----------
        data : slice
            list of pages of responses from inat utility.
        Returns
        -------
        returns : list[result_return_for_image]
            a list of class objects: list[result_return_for_image()]
    """
    return_list = list()
    for x in data['results']:
        try:
            geoLocationLatLong = x['observation']['location']
            observationPhoto = x['observation']['observation_photos'][0]['photo']['url'].replace('square', 'original')
            createAtDate = x['created_at_details']['date']
            return_list.append(result_return_for_image(geoLocationLatLong, observationPhoto, createAtDate))
        except Exception as error:
            print(error)
    return return_list


def get_requests_from_entry_file(destinationFolder):
    with open(destinationFolder) as f:
        lines = f.readlines()
    return lines 