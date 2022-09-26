import math

def get_total_pages(response, page_size):
    try:
        total_results = response["total_results"]
        number_of_pages = math.ceil(response["total_results"]/page_size)
        print(f'total_results: {total_results}')
        print(f'number_of_pages: {number_of_pages}')
        print(f'number_of_images: {number_of_pages * 5}')

        return number_of_pages
    except Exception as error:
        print(error)
        return False

def get_common_request_information(response, page_size):
    return_object = type('obj', (object,), {'total_results': 'value', 'number_of_pages': 'value'})
    try:
        return_object.total_results = response["total_results"]
        return_object.number_of_pages = math.ceil(response["total_results"]/page_size)
        return_object.page_number = response["page"]
        print(f'total_results: {return_object.total_results}')
        print(f'number_of_pages: {return_object.number_of_pages}')
        return return_object
    except Exception as error:
        print(error)
        return False


def get_all_urls_list(response):
    return response


def get_all_image_urls_list(response):
    return response


def get_results_len(response):
    try:
        return len(response["results"])
    except Exception as error:
        print(error)
        return False
