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
  tags = {
    Owner = var.userName,
    Name = var.applicationName
  }
  user_data = <<-EOF
                #!/bin/bash
                yum install -y mysql56-server
              EOF
}