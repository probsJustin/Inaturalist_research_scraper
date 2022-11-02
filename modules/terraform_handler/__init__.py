import json
from subprocess import Popen, check_output



def create_database():
    print(f'Attempting to creat database instance.....')
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


def create_master_node():
    print(f'Attempting to creat database instance.....')
    terraform_directory =f'./terraform/master_node'
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


def create_worker_node(worker_node_id):
    print(f'Attempting to creat database instance.....')
    terraform_directory =f'./terraform/worker_node'
    with open('./terraform/configuration.json') as json_file:
        configuration = json.load(json_file)

    terraform_command_init = f'''terraform -chdir={terraform_directory} init -var=worker_node_id:{worker_node_id}'''
    terraform_command_plan = f'''terraform -chdir={terraform_directory} plan -var=worker_node_id:{worker_node_id}'''
    terraform_command_apply = f'''terraform -chdir={terraform_directory} apply -var=worker_node_id:{worker_node_id} -auto-approve'''

    print(f'Terraform init...')
    init = check_output(terraform_command_init)
    print(f'Terraform plan ...')
    plan = check_output(terraform_command_plan)
    print(f'Terraform apply....')
    apply = check_output(terraform_command_apply)
    print(f'Done creating instance.....')
    return init, plan, apply