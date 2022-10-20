variable "region" {
  type        = string
  description = "The where to deploy the VPC"
}

variable "availability_zones" {
  type        = list(string)
  description = "AZs"
}

variable "vpc_name" {
  type        = string
  description = "VPC name"
}

variable "cidr_block" {
  type        = string
  description = "VPC cidr block. Example: 10.0.0.0/16"
}

variable "tags" {
  type = map(string)
  default = {
    Owner       = "PECS"
    Project     = "Apha"
    Environment = "dev"
    Create_By   = "Terraform"
  }
}
