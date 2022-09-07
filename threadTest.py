import re
from concurrent.futures import ThreadPoolExecutor
import time
import requests
import shutil
import math
import time
import hashlib
PAGE_LENGTH = 30
PAGE_PARAM = f'page'
NUMBER_OF_THEADS = 5

def download_image(url):
    print(url)
    request_payload = requests.get(url).text
    matches = re.findall('medium_url":"([^"]*)', request_payload, re.DOTALL)
    counter = 1

    newMatches = dict()
    for z in matches:
        newMatches[z] = ""

    for url in newMatches.keys():
        print(f'{counter}/{len((newMatches.keys()))}')
        print(url + '\n')
        counter = counter + 1
        response = requests.get(url, stream=True)
        fileName = hashlib.md5(url.encode('utf-8'))
        with open(f'./content/inat_{fileName.hexdigest()}.jpg', 'wb+') as out_file:
            shutil.copyfileobj(response.raw, out_file)


def initial_total_results_request(url):
    return requests.get(url).json()


def get_pages_request(url):
    print("Entering Get Total")
    result = initial_total_results_request(url)
    total_results = result["total_results"]
    page_max_length = math.ceil(total_results / PAGE_LENGTH)
    page_itr = 1
    print(f'Total Results: {total_results}')
    print(f'Total Number of Pages: {page_max_length}')

    executor = ThreadPoolExecutor(NUMBER_OF_THEADS)
    future_tasks = list()
    for y in range(page_itr, page_max_length):
        future_tasks.append(executor.submit(download_image(f'{url}&{PAGE_PARAM}={y}')))

    time.sleep(1)
    for tasks in future_tasks:
        try:
            tasks.done()
            tasks.result()
        except Exception as error:
            print(error)



def log(message):
    print(f'{time.ctime()} :: {message}')


filename = "requests.txt"
request_list = list()
# Open the file as f.
# The function readlines() reads the file.
with open(filename, 'r') as f:
    content = f.readlines()

for x in content:
    request_list.append(x.strip())

for y in request_list:
    get_pages_request(y)
