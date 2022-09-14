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
import modules.response_handler as response_handler
from rich import print
import time

### Setup
internal_logger.basicConfig(filename=f'./logs/inat_{time.strftime("%Y%m%d-%H%M%S")}.log', level=internal_logger.DEBUG)
enable_logging()

def get_all_pages_as_dict(number_of_pages):
    dict_to_return = dict()
    for x in range(0, number_of_pages):
        time.sleep(0.5)
        dict_to_return[x] = get_identifications(taxon_id=[52818], per_page=200, page=x)
        internal_logger.debug(f'Printing Page Number: {x}')
    return dict_to_return

internal_logger.debug(f'Testing.....')
response = get_identifications(taxon_id=[52818], per_page=200, page=1)
number_of_pages_needed = response_handler.get_total_pages(response, 200)

pagedResponse = dict()
for x in range(1, number_of_pages_needed):
    print(f'page: {x}')
    try:
        pagedResponse[x] = get_identifications(taxon_id=[52818], per_page=200, page=x)
    except Exception as error:
        print(error)
        break

for y in pagedResponse:
    print(f'\nPAGE: {y}\n')
    pprint(pagedResponse[y])

