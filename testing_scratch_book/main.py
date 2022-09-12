##imports for making this work
from typing import List, Any, Union

import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse



## url validator

def is_valid(url):
    ##    Checks whether `url` is a valid URL.
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)
    ## grabber core - it grabs images


def get_all_images(url):
    """
    Returns all image URLs on a single `url`
    """

    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    ##this is the section that extracts img tags into HTML

    urls: list[Union[Union[str, int, bytes], Any]] = []

    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src")
        if not img_url:
            continue

    ##absolute url checker
    ## make the URL absolute by joining domain with the URL that is just extracted
    img_url = urljoin(url, img_url)

    try:
        pos = img_url.index("?")
        img_url = img_url[:pos]
    except ValueError:
        pass

    if is_valid(img_url):
        urls.append(img_url)
    else:
        print("Not Img")
    return urls


def download(url, pathname):
    ## Downloads a file given an URL and puts it in the folder `pathname`
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
        # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))


def main(url, path):
    # get all images
    imgs = get_all_images(url)
    for img in imgs:
            # for each image, download it
            download(img, path)

main("https://www.inaturalist.org/observations?photos&place_id=any&verifiable=any", "../test")


for items in soup.select(".photo-list-photo-view"):
    image= "https:" + items['style'].split("url(")[1].split(")")[0]
