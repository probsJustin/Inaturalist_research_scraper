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

with open('./content/links/link_page.json') as json_file:
    data = json.load(json_file)

contentDirectory = './content/images'
times = list()
counter = 0
for url in data:
    start = (time.time())
    counter = counter + 1
    fileName = hashlib.md5(url.encode('utf-8'))
    fileNameHash = f'inat_{fileName.hexdigest()}.jpg'
    filePath = f'./content/images/inat_{fileName.hexdigest()}.jpg'
    if fileNameHash not in contentDirectory:
        response = requests.get(url, stream=True)
        with open(filePath, 'wb+') as out_file:
            shutil.copyfileobj(response.raw, out_file)
    end = (time.time())
    times.append(end - start)
    print(f'Average Time in Seconds: {Average(times)}')
