import modules.database_connection_handler as db
import modules.configuration_handler as config


def create_request_table():
    connection = db.create_connection(config.get_configuration('db_address'), config.get_configuration('db_name'),
                                      config.get_configuration('db_user'), config.get_configuration('db_pass'))
    sql = f'''
    CREATE TABLE requests (
        id int NOT NULL AUTO_INCREMENT,
        requestUrl VARCHAR(255),
        requestPayload TEXT(200000),
        workerNodeId VARCHAR(255),
        isDone VARCHAR(255),
        PRIMARY KEY (id)
    
    );
    '''
    response = db.execute_sql(sql, connection)
    return response


def create_request_entry(request_url, request_payload, worker_node_id):
    connection = db.create_connection(config.get_configuration('db_address'), config.get_configuration('db_name'),
                                      config.get_configuration('db_user'), config.get_configuration('db_pass'))
    sql = f'''
    INSERT INTO requests (requestUrl, requestPayload, workerNodeId)
    VALUES ({request_url}, {request_payload}, {worker_node_id});
    );
    '''
    response = db.execute_sql(sql, connection)
    return response


def mark_request_complete(request_url):
    connection = db.create_connection(config.get_configuration('db_address'), config.get_configuration('db_name'),
                                      config.get_configuration('db_user'), config.get_configuration('db_pass'))
    sql = f'''
    UPDATE requests SET isDone=true WHERE requestUrl={request_url}
    '''
    response = db.execute_sql(sql, connection)
    return response