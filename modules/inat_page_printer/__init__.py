import math


def get_total_pages(response, page_size):
    return_object = type('obj', (object,), {'total_results': 'value', 'number_of_pages': 'value'})
    try:
        return_object.total_results = response["total_results"]
        return_object.number_of_pages = math.ceil(response["total_results"]/page_size)
        print(f'total_results: {return_object.total_results}')
        print(f'number_of_pages: {return_object.number_of_pages}')
        return return_object
    except Exception as error:
        print(error)
        return False

