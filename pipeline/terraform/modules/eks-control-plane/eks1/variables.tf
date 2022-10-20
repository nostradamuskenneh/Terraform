variable "region" {
  type = string
}

variable "eks-control-plane-version" {
  type = string
}

variable "eks-node-group-version" {
  type = string
}

variable "eks-node-group-instance-types" {
  type = list(any)
}

variable "node-group-desired-size" {
  type = string
}

variable "node-group-max-size" {
  type = string
}

variable "node-group-min-size" {
  type = string
}

variable "node-group-disk-size" {
  type = string
}

variable "availability-zones" {
  type = list(any)
}

variable "vpc-cidr-block" {
  type = string
}

variable "vpc-public-subnets" {
  type = list(any)
}

variable "vpc-private-subnets" {
  type = list(string)
}

variable "instance_tenancy" {
  type    = string
  default = "default"
}

variable "enable_dns_support" {
  type    = bool
  default = true
}

variable "enable_dns_hostnames" {
  type    = bool
  default = true
}

variable "enable_classiclink" {
  type    = bool
  default = false
}

variable "enable_classiclink_dns_support" {
  type    = bool
  default = false
}

variable "assign_generated_ipv6_cidr_block" {
  type    = bool
  default = false
}

variable "tags" {
  type = map(string)
  default = {
    Owner       = "SRP"
    Access-ID   = "2645"
    Project     = "srp"
    Environment = "dev"
    Create_By   = "Terraform"
  }
}
