import modules.database_connection_handler as db
import modules.configuration_handler as config


connection = db.create_connection(config.get_configuration('db_address'), config.get_configuration('db_name'), config.get_configuration('db_user'), config.get_configuration('db_pass'))
sql = ''
response = db.execute_sql(connection, sql)
