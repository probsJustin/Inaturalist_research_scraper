variable "region" {
  default = "us-east-2"
}

variable "applicationName" {
  default = "masterNodeApplication"
}

variable "userName" {
  default = "justinshagerty@gmail.com"
}

variable "image" {
  default = "ami-089a545a9ed9893b6"
}

variable "instanceType" {
  default = "t2.micro"
}

variable "key_pair_name" {
  default = "Deployment-Key-Pair"
}

variable "database_ip_address"{
  default = "192.168.0.1"
}

variable "operation"{
  default = "master"
}