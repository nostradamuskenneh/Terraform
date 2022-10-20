resource "aws_vpc" "main" {
  cidr_block           = var.cidr_block
  enable_dns_support   = true
  enable_dns_hostnames = true
  enable_classiclink   = false

  tags = {
    Name        = format("%s-%s-vpc", var.vpc_name, var.tags.Environment)
    Owner       = var.tags.Owner
    Project     = var.tags.Project
    Environment = var.tags.Environment
    Create_By   = var.tags.Create_By
  }
}

######################################################
# Enable access to or from the Internet for instances
# in public subnets
######################################################
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name        = format("%s-%s-internet-gateway", var.vpc_name, var.tags.Environment)
    Owner       = var.tags.Owner
    Project     = var.tags.Project
    Environment = var.tags.Environment
    Create_By   = var.tags.Create_By
  }
}
