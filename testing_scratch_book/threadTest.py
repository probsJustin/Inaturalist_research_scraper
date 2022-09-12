import os
import re
from concurrent.futures import ThreadPoolExecutor
import requests
import shutil
import math
import time
import hashlib
from os.path import exists


PAGE_LENGTH = 30
PAGE_PARAM = f'page'
NUMBER_OF_THEADS = 5

def download_image(url):
    start = (time.time())
    request_payload = requests.get(url).text
    matches = re.findall('medium_url":"([^"]*)', request_payload, re.DOTALL)
    counter = 1

    newMatches = dict()
    for z in matches:
        newMatches[z] = ""

    for url in newMatches.keys():
        counter = counter + 1
        fileName = hashlib.md5(url.encode('utf-8'))
        fileNameHash = f'inat_{fileName.hexdigest()}.jpg'
        filePath = f'./content/inat_{fileName.hexdigest()}.jpg'
        if fileNameHash not in contentDirectory:
            response = requests.get(url, stream=True)
            with open(filePath, 'wb+') as out_file:
                shutil.copyfileobj(response.raw, out_file)
    end = (time.time())
    print(f'Seconds: {end - start}')


def initial_total_results_request(url):
    return requests.get(url).json()

def doNothing():
    thing = 1

def get_pages_request(url):
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

    time.sleep(2)
    for tasks in future_tasks:
        try:
            tasks.done()
            tasks.result()
        except Exception as error:
            doNothing()



def log(message):
    print(f'{time.ctime()} :: {message}')


contentDirectory = os.listdir('./content')
filename = "requests_2.txt"
request_list = list()


with open(filename, 'r') as f:
    content = f.readlines()

for x in content:
    request_list.append(x.strip())

requestCounter = 0
for y in request_list:
    requestCounter = requestCounter + 1
    print(f'Request Number: {requestCounter}')
    get_pages_request(y)
