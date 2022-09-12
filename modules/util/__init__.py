def get_all_pages_as_dict(number_of_pages):
    dict_to_return = dict()
    for x in range(0, number_of_pages):
        dict_to_return[x] = get_identifications(taxon_id=[52818], per_page=200, page=x)
    return dict_to_return