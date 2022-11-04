terraform {
  backend "local" {
    path = "./terraform_state.tfstate"
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }
}

provider "aws" {
  region  = var.region
}

resource "aws_instance" "test_aws_instance" {
  ami           = var.image
  instance_type = var.instanceType
  key_name      = var.key_pair_name

  user_data = <<-EOF
                #!/bin/bash
                export worker_node_id = var.worker_node_id
                export database_ip_address = var.database_ip_address
              EOF
  tags = {
    Owner = var.userName,
    Name = var.applicationName
  }
}