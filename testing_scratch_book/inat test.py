import re

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
from rich import print

enable_logging()


response = get_identifications(taxon_id=[52818], per_page=200, page=10)
pprint(response)

