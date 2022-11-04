import modules.terraform_handler as tf_handler
import modules.configuration_handler as config
import time


print(tf_handler.create_database())
time.sleep(5)
resource = dict()
tf_state = tf_handler.get_tf_state_file(f'./terraform/database', f'terraform_state.tfstate')
resources = tf_handler.get_aws_instance_resources_from_tfstate_file(tf_state)
for resource in resources:
    if(resource['values']['tags']['Name'] == "databaseApplication"):
        print(resource["values"]["public_ip"])
        config.set_configuration("db_address", resource["values"]["public_ip"])


