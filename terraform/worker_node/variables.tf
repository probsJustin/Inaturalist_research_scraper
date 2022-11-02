variable "region" {
  default = "us-east-2"
}

variable "applicationName" {
  default = "databaseApplication"
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

variable "worker_node_id"{
  default = 0
}