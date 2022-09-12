### Imports
import re
import time
import altair as alt
import ipyplot
import pandas as pd
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

import logging as internal_logger
import modules.inat_page_printer as pageHandler
from rich import print

### Setup
enable_logging()
internal_logger.basicConfig(filename=f'inat_{time.ctime()}.log', level=internal_logger.DEBUG)




def get_all_pages_as_dict(number_of_pages):
    dict_to_return = dict()
    for x in range(0, number_of_pages):
        time.sleep(0.5)
        dict_to_return[x] = get_identifications(taxon_id=[52818], per_page=200, page=x)
        internal_logger.debug(f'Printing Page Number: {x}')
    return dict_to_return




response = get_identifications(taxon_id=[52818], per_page=200, page=10)
pageHandlerInfo = pageHandler.get_total_pages(response, 200)
#len(get_all_pages_as_dict(pageHandlerInfo.number_of_pages))
pprint(response)