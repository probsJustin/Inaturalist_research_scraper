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

def get_dict_paged_identifications(param_taxon_id, number_of_needed_pages):
    pagedResponse = dict()
    for x in range(1, number_of_needed_pages):
        try:
            pagedResponse[x] = get_identifications(taxon_id=[param_taxon_id], per_page=200, page=x)
        except Exception as error:
            print(error)
            break
    return pagedResponse