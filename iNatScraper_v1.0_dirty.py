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

import logging as internal_logger
import modules.response_handler as response_handler
import modules.util as util

from rich import print
import time

### Setup
internal_logger.basicConfig(filename=f'./logs/inat_{time.strftime("%Y%m%d-%H%M%S")}.log', level=internal_logger.DEBUG)
enable_logging()


internal_logger.debug(f'Testing.....')
response = get_identifications(taxon_id=[52818], per_page=200, page=1)
number_of_pages_needed = response_handler.get_total_pages(response, 200)

pagedResponse = dict()

pagedResponse = util.get_dict_paged_identifications(52818, number_of_pages_needed)

unique = dict()
for y in pagedResponse:
    #print(f'\nPAGE: {y}\n')
    #pprint(pagedResponse[y])
    #util.write_content_to_files(pagedResponse[y], 52818, y)
    for x in pagedResponse[y]['results']:
        for j in util.get_image_url(x, "(http?s?:?\/\/[^\"']*\.(?:png|jpg|jpeg|gif|png|svg))" ):
            unique[j] = ''

print(unique.keys())
with open(f'./content/links/link_page.json', "w") as outfile:
    outfile.write(json.dumps(str(unique.keys()), indent=4))
