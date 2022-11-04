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