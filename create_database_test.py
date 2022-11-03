import codecs
import modules.terraform_handler as tf_handler
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
        my_connection_instance['ppk_file_path'] = "/ppk/Deployment-Key-Pair-OpenSSH"


        # time.sleep(1)
        # print(run_ssh(my_connection_instance, 'sudo su'))
        # time.sleep(1)
        # print(run_ssh(my_connection_instance, 'sudo amazon-linux-extras install docker -y'))
        # time.sleep(1)
        # print(run_ssh(my_connection_instance, 'sudo service docker start'))
        # time.sleep(1)
        # print(run_ssh(my_connection_instance, 'sudo yum install -y git'))
        # time.sleep(1)
        # print(run_ssh(my_connection_instance, 'sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose'))
        # time.sleep(1)
        # print(run_ssh(my_connection_instance, 'sudo chmod +x /usr/local/bin/docker-compose'))
        # time.sleep(1)
        # print(run_ssh(my_connection_instance, 'ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose'))
        # time.sleep(1)
        # print(f'You will have to connect to this instance and run "sudo mysql_secure_installation"')
        '''
        sudo amazon-linux-extras install docker -y
        sudo service docker start
        sudo yum install -y git
        sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
        sudo chmod +x /usr/local/bin/docker-compose
        ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
        curl -o ./docker-compose.yaml https://github.com/probsJustin/Inaturalist_research_scraper/blob/main/docker-compose/phpmyadmin/docker-compose.yaml
        docker-compose up -d
        '''

