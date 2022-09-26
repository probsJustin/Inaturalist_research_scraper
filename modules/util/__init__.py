import json
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
import re
import modules.internal_logger as logger



def contact():
    return f'Please reach out to the admin of this application.'


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
    try:
        pagedResponse = dict()
        for x in range(1, number_of_needed_pages):
            try:
                pagedResponse[x] = get_identifications(taxon_id=[param_taxon_id], per_page=per_page_param, page=x)
            except Exception as error:
                logger.log_this('error', error)
                break
    except Exception as error:
        raise Exception(f'Not able to get paged response from inaturalist api: {error} \n {contact()}')
    return pagedResponse

def get_dict_paged_observations(param_taxon_id, number_of_needed_pages, per_page_param):
    try:
        pagedResponse = dict()
        for x in range(1, number_of_needed_pages):
            try:
                pagedResponse[x] = get_observations(taxon_id=[param_taxon_id], per_page_param=200, page=x)
            except Exception as error:
                logger.log_this('error', error)
                break
    except Exception as error:
        raise Exception(f'Not able to get paged observations from the inaturalist api: {error} \n {contact()}')
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
    try:
        return_list = list()
        for x in data['results']:
            try:
                geoLocationLatLong = x['observation']['location']
                observationPhoto = x['observation']['observation_photos'][0]['photo']['url'].replace('square', 'original')
                createAtDate = x['created_at_details']['date']
                return_list.append(result_return_for_image(geoLocationLatLong, observationPhoto, createAtDate))
            except Exception as inner_error:
                logger.log_this('warning', f'Warning: {inner_error}')
    except Exception as error:
        raise Exception(f'Not able to process inaturalist result data: {error} \n {contact()}')
    return return_list


def get_requests_from_entry_file(destinationFolder):
    with open(destinationFolder) as f:
        lines = f.readlines()
    return lines

def get_taxon_id_from_url(url):
    regex_taxon_id = 'taxon_id=(\d*)'
    return re.search(regex_taxon_id, url)