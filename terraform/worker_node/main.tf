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
  vpc_security_group_ids = [aws_security_group.ssh_security_group.id]
  user_data = <<-EOF
                #!/bin/bash
                echo worker_node_id="${var.worker_node_id}" >> /etc/environment
                echo database_ip_address="${var.database_ip_address}" >> /etc/environment
                echo inat_operation="${var.operation}" >> /etc/environment
              EOF
  tags = {
    Owner = var.userName,
    Name = var.applicationName
  }
}

resource "aws_security_group" "ssh_security_group" {
  ingress {
    cidr_blocks = [
      "0.0.0.0/0"
    ]
    from_port = 22
    to_port = 22
    protocol = "tcp"
  }
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = [
      "0.0.0.0/0"]
  }
}