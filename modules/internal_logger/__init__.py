import time

log_level = dict()
log_level['all'] = False
log_level['info'] = True
log_level['error'] = True
log_level['debug'] = True
log_level['warning'] = True
log_level['image_handler'] = True
log_level['download_handler'] = True
log_level['response_handler'] = True

def process_log_message(log_entry):
    print(log_entry)

def log_this(log_level_param, log_message):
    if(log_level[log_level_param] == True or log_level['all'] == True):
        log_string = f'[{time.strftime("%Y-%m-%d %H:%M:%S")}] \t [{log_level_param}] \t {log_message}'
        process_log_message(log_string)
