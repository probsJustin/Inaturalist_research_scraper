import codecs
import modules.terraform_handler as tf_handler
import modules.configuration_handler as config
import paramiko
import json
import time


def run_ssh(connection, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(connection['hostname'], username=connection['username'], password=connection['password'], key_filename=connection['ppk_file_path'])
    stdin, stdout, stderr = ssh.exec_command(command)
    response = stdout.readlines()
    ssh.close()
    return response


print(tf_handler.create_database())
time.sleep(5)
resource = dict()
tf_state = tf_handler.get_tf_state_file(f'./terraform/database', f'terraform_state.tfstate')
resources = tf_handler.get_aws_instance_resources_from_tfstate_file(tf_state)
for resource in resources:
    if(resource['values']['tags']['Name'] == "databaseApplication"):
        my_connection_instance = dict()
        print(resource["values"]["public_ip"])
        my_connection_instance['hostname'] = f'{resource["values"]["public_ip"]}'
        my_connection_instance['username'] = "ec2-user"
        my_connection_instance['password'] = ""
        my_connection_instance['ppk_file_path'] = config.get_configuration('path_to_ssh_ppk')
        config.set_configuration("db_address", resource["values"]["public_ip"])


