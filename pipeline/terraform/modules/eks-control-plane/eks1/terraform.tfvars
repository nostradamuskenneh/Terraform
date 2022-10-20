region = "us-east-1"

# EKS
eks-control-plane-version = "1.20"

# EKS Node Group
eks-node-group-version        = "1.20"
node-group-desired-size       = "1"
node-group-max-size           = "2"
node-group-min-size           = "1"
node-group-disk-size          = "20"
eks-node-group-instance-types = ["t3.small"]

# VPC
availability-zones               = ["us-east-1a", "us-east-1b"]
vpc-cidr-block                   = "192.168.0.0/16"
vpc-private-subnets              = ["192.168.0.0/18", "192.168.64.0/18"]
vpc-public-subnets               = ["192.168.128.0/18", "192.168.192.0/18"]
instance_tenancy                 = "default"
enable_dns_support               = true
enable_dns_hostnames             = true
enable_classiclink               = false
enable_classiclink_dns_support   = false
assign_generated_ipv6_cidr_block = false

# Tags
tags = {
  Owner       = "SRP"
  Access-ID   = "2645"
  Project     = "srp"
  Environment = "dev"
  Create_By   = "Terraform"
}
