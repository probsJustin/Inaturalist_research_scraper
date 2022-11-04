import modules.terraform_handler as tf_handler
import time


print(tf_handler.create_worker_node(1, config.get_configuration("db_address")))
time.sleep(5)
resource = dict()
tf_state = tf_handler.get_tf_state_file(f'./terraform/worker_node', f'terraform_state.tfstate')
resources = tf_handler.get_aws_instance_resources_from_tfstate_file(tf_state)
for resource in resources:
    if(resource['values']['tags']['Name'] == "databaseApplication"):
        print(resource["values"]["public_ip"])



