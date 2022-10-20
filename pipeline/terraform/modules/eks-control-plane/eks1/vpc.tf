resource "aws_vpc" "main" {
  cidr_block                       = var.vpc-cidr-block
  instance_tenancy                 = var.instance_tenancy
  enable_dns_support               = var.enable_dns_support
  enable_dns_hostnames             = var.enable_dns_hostnames
  enable_classiclink               = var.enable_classiclink
  enable_classiclink_dns_support   = var.enable_classiclink_dns_support
  assign_generated_ipv6_cidr_block = var.assign_generated_ipv6_cidr_block
  tags = {
    Name        = format("%s-%s-%s-vpc", var.tags.Access-ID, var.tags.Project, var.tags.Environment)
    Owner       = var.tags.Owner
    Access-ID   = var.tags.Access-ID
    Project     = var.tags.Project
    Environment = var.tags.Environment
    Create_By   = var.tags.Create_By
  }
}
