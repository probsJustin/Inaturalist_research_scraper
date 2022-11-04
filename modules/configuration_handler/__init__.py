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


def set_configuration(config_index, value):
    instance_config = init_configuration()
    instance_config[config_index] = value
    with open('./configuration.json', 'w') as convert_file:
        convert_file.write(json.dumps(instance_config))
