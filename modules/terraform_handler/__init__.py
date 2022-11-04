import json
from subprocess import Popen, check_output


def get_aws_instance_resources_from_tfstate_file(tf_state):
    tf_state = json.loads(tf_state.decode('utf8'))
    resource_list = list()
    for resource in tf_state["values"]["root_module"]["resources"]:
        if(resource['type'] == 'aws_instance'):
            resource_list.append(resource)
    return resource_list


def get_tf_state_file(terraform_directory, file_name):
    terraform_show_command = f'''terraform -chdir={terraform_directory} show -json {file_name}'''
    print(f'Running show command for file: {file_name} ....')
    return check_output(terraform_show_command)


def create_database():
    print(f'Attempting to create database instance.....')
    terraform_directory =f'./terraform/database'
    with open('./terraform/configuration.json') as json_file:
        configuration = json.load(json_file)

    terraform_command_init = f'''terraform -chdir={terraform_directory} init '''
    terraform_command_plan = f'''terraform -chdir={terraform_directory} plan '''
    terraform_command_apply = f'''terraform -chdir={terraform_directory} apply -auto-approve'''

    print(f'Terraform init...')
    init = check_output(terraform_command_init)
    print(f'Terraform plan ...')
    plan = check_output(terraform_command_plan)
    print(f'Terraform apply....')
    apply = check_output(terraform_command_apply)
    print(f'Done creating instance.....')
    return init, plan, apply


def destroy_database():
    print(f'Attempting to create database instance.....')
    terraform_directory =f'./terraform/database'
    with open('./terraform/configuration.json') as json_file:
        configuration = json.load(json_file)

    terraform_command_init = f'''terraform -chdir={terraform_directory} init -destroy'''
    terraform_command_plan = f'''terraform -chdir={terraform_directory} plan -destroy'''
    terraform_command_apply = f'''terraform -chdir={terraform_directory} apply -destroy -auto-approve'''

    print(f'Terraform init...')
    init = check_output(terraform_command_init)
    print(f'Terraform plan ...')
    plan = check_output(terraform_command_plan)
    print(f'Terraform apply....')
    apply = check_output(terraform_command_apply)
    print(f'Done creating instance.....')
    return init, plan, apply


def create_master_node(database_ip_address):
    print(f'Attempting to creat database instance.....')
    terraform_directory =f'./terraform/master_node'
    with open('./terraform/configuration.json') as json_file:
        configuration = json.load(json_file)

    terraform_command_init = f'''terraform -chdir={terraform_directory} init -var=database_ip_address={database_ip_address}'''
    terraform_command_plan = f'''terraform -chdir={terraform_directory} plan -var=database_ip_address={database_ip_address}'''
    terraform_command_apply = f'''terraform -chdir={terraform_directory} apply -var=database_ip_address={database_ip_address} -auto-approve'''

    print(f'Terraform init...')
    init = check_output(terraform_command_init)
    print(f'Terraform plan ...')
    plan = check_output(terraform_command_plan)
    print(f'Terraform apply....')
    apply = check_output(terraform_command_apply)
    print(f'Done creating instance.....')
    return init, plan, apply


def destroy_master_node():
    print(f'Attempting to create database instance.....')
    terraform_directory =f'./terraform/master_node'
    with open('./terraform/configuration.json') as json_file:
        configuration = json.load(json_file)

    terraform_command_init = f'''terraform -chdir={terraform_directory} init -destroy '''
    terraform_command_plan = f'''terraform -chdir={terraform_directory} plan -destroy '''
    terraform_command_apply = f'''terraform -chdir={terraform_directory} apply -destroy -auto-approve'''

    print(f'Terraform init...')
    init = check_output(terraform_command_init)
    print(f'Terraform plan ...')
    plan = check_output(terraform_command_plan)
    print(f'Terraform apply....')
    apply = check_output(terraform_command_apply)
    print(f'Done creating instance.....')
    return init, plan, apply


def create_worker_node(worker_node_id, database_ip_address):
    print(f'Attempting to create database instance.....')
    terraform_directory =f'./terraform/worker_node'
    with open('./terraform/configuration.json') as json_file:
        configuration = json.load(json_file)

    terraform_command_init = f'''terraform -chdir={terraform_directory} init -var=worker_node_id={worker_node_id} -var=database_ip_address={database_ip_address}'''
    terraform_command_plan = f'''terraform -chdir={terraform_directory} plan -var=worker_node_id={worker_node_id} -var=database_ip_address={database_ip_address}'''
    terraform_command_apply = f'''terraform -chdir={terraform_directory} apply -var=worker_node_id={worker_node_id} -var=database_ip_address={database_ip_address} -auto-approve'''

    print(f'Terraform init...')
    init = check_output(terraform_command_init)
    print(f'Terraform plan ...')
    plan = check_output(terraform_command_plan)
    print(f'Terraform apply....')
    apply = check_output(terraform_command_apply)
    print(f'Done creating instance.....')
    return init, plan, apply


def destroy_worker_node():
    print(f'Attempting to destroy database instance.....')
    terraform_directory =f'./terraform/worker_node'
    with open('./terraform/configuration.json') as json_file:
        configuration = json.load(json_file)

    terraform_command_init = f'''terraform -chdir={terraform_directory} init -destroy '''
    terraform_command_plan = f'''terraform -chdir={terraform_directory} plan -destroy '''
    terraform_command_apply = f'''terraform -chdir={terraform_directory} apply -destroy -auto-approve'''

    print(f'Terraform init...')
    init = check_output(terraform_command_init)
    print(f'Terraform plan ...')
    plan = check_output(terraform_command_plan)
    print(f'Terraform apply....')
    apply = check_output(terraform_command_apply)
    print(f'Done creating instance.....')
    return init, plan, apply
