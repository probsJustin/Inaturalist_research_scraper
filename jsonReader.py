import re
import time
import altair as alt
import ipyplot
import pandas as pd
import shutil
import os
import re
from concurrent.futures import ThreadPoolExecutor
import requests
import shutil
import math
import time
import hashlib
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

def Average(lst):
    return sum(lst) / len(lst)

with open('./content/requests/page_identification_52818_1.json') as json_file:
    data = json.load(json_file)

def keys(newList):
    for x in newList.keys():
        print(x)

thing = data['results'][0]['observation']['identifications'][0]['previous_observation_taxon']['default_photo']['url']
for x in data['results']:
    try:
        for y in x['observation']['identifications'][0]:
            print(x['observation']['identifications'][y]['previous_observation_taxon']['default_photo']['url'])
    except Exception as error:
        print(x['observation']['identifications'][0].keys())


#keys(thing)