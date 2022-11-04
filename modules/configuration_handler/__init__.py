import json



def init_configuration():
    with open('./configuration.json') as json_file:
        configuration = json.load(json_file)

    return configuration

def get_configuration(config_index):
    try:
        return init_configuration()[config_index]
    except Exception as error:
        return None
