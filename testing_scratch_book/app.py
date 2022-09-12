import datetime

import requests
import os
import json
import re
import time
import requests
import math
import asyncio
import aiohttp, aiofiles
import random

PAGE_LENGTH = 30
PAGE_PARAM = f'page'


async def gather_with_concurrency(n, *tasks):
    semaphore = asyncio.Semaphore(n)

    async def sem_task(task):
        async with semaphore:
            return await task
    return await asyncio.gather(*(sem_task(task) for task in tasks))


async def getApiJsonFromINat(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            if(response.status == 429):
                await getApiJsonFromINat(url)
            json = await response.json()
    return json

async def asyncGetApiJsonFromINat(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            if(response.status == 429):
                await asyncGetApiJsonFromINat(url)
            json = await response.json()
    return json

async def asyncGetApiContentFromINat(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)
            if(response.status == 429):
                await asyncGetApiContentFromINat(url)
            text = await response.text()
    return text



async def asyncGetApiImageFromINat(url, imageName):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                f = await aiofiles.open(f'./content/inat_{imageName}.jpg', mode='wb')
                await f.write(await response.read())
                await f.close()
            if(response.status == 429):
                await asyncGetApiImageFromINat(url, imageName)


def getApiJsonFromINatBytes(url):
    return requests.get(url).content

def init_request(url):
    results = getApiJsonFromINat(url)

    return results["total_results"]


async def request_download(testJson):
    # Decode UTF-8 bytes to Unicode, and convert single quotes
    # to double quotes to make it valid JSON
    my_results_json = testJson

    # Load the JSON to a Python list & dump it back out as formatted JSON


    matches = re.findall('medium_url":"([^"]*)', my_results_json, re.DOTALL)
    counter = 1

    newMatches = dict()
    for z in matches:
        newMatches[z] = ""

    for x in newMatches.keys():
        print(f'{counter}/{len((newMatches.keys()))}')
        print(x + '\n')
        counter = counter + 1
        r = await asyncGetApiImageFromINat(x, counter + random.randint(0, 999999999999999999999))
        print(r)

async def get_specific_page_request(url, page_number, **kwargs):
    print(f'[PAGE_NUMBER: {page_number}]::{url}')
    request_payload = await asyncGetApiContentFromINat(f'{url}&{PAGE_PARAM}={page_number}')
    return await request_download(request_payload)

async def get_total_create_requests(url, **kwargs):
    print("Entering Get Total")
    result = await getApiJsonFromINat(url)
    total_results = result["total_results"]
    page_max_length = math.ceil(total_results / PAGE_LENGTH)
    page_itr = 1
    tasks = []
    for x in range(page_itr, page_max_length):
        tasks.append(get_specific_page_request(url, x, **kwargs))
    return await gather_with_concurrency(1, *tasks)

async def get_all_requests(list_requests, **kwargs):
    more_tasks = []
    for x in list_requests:
        more_tasks.append(get_total_create_requests(x, **kwargs))
    return await gather_with_concurrency(1, *more_tasks)



filename = "../requests.txt"
request_list = list()
# Open the file as f.
# The function readlines() reads the file.
with open(filename, 'r') as f:
    content = f.readlines()


for x in content:
    request_list.append(x.strip())

loop = asyncio.ProactorEventLoop()
asyncio.set_event_loop(loop)
asyncio.Semaphore(1)
asyncio.run(get_all_requests(request_list))  # Python 3.7+



