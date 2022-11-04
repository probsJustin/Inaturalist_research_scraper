import modules.database_connection_handler as db
import modules.configuration_handler as config


connection = db.create_connection(config.get_configuration('db_address'), config.get_configuration('db_name'), config.get_configuration('db_user'), config.get_configuration('db_pass'))
print(connection)
sql = f'''
CREATE TABLE requests (
    id int NOT NULL AUTO_INCREMENT,
    requestUrl VARCHAR(255),
    requestPayload TEXT(200000),
    workerNodeId VARCHAR(255),
    PRIMARY KEY (id)

);
'''
response = db.execute_sql(sql, connection)
print(response)
