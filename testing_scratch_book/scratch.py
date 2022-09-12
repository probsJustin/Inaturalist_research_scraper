future_tasks = list()
for y in range(page_itr, page_max_length):
    future_tasks.append(executor.submit(download_image(f'{url}&{PAGE_PARAM}={y}')))

time.sleep(1)
for tasks in future_tasks:
    try:
        tasks.done()
        tasks.result()
    except:
        print(tasks)