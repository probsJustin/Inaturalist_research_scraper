import pyodbc
import time
import requests


def execute_sql(sql, connection):
    cnxn = pyodbc.connect(f'''
    DRIVER={{SQL Server}};
    SERVER={connection['database_address']};
    DATABASE={connection['database_name']}
    UID={connection['database_user']};
    PWD={connection['database_pass']};
    ''')
    cursor = cnxn.cursor()
    cursor.execute(sql)
    sql_result = cursor.fetchall()
    cnxn.close()
    return sql_result

def create_connection(database_address, database_name, database_user, database_pass):
    connection = dict()
    connection['database_pass'] = database_pass
    connection['database_user'] = database_user
    connection['database_address'] = database_address
    connection['database_name'] = database_name
    return connection
