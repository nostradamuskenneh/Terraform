module "vpc" {
  source = "terraform-aws-modules/vpc/aws"

  # VPC Basic Details
  name            = "beta-development-vpc"
  cidr            = "10.0.0.0/16"
  azs             = ["us-east-1a", "us-east-1b"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24"]

  # Database Subnets
  create_database_subnet_group       = true
  create_database_subnet_route_table = true
  database_subnets                   = ["10.0.151.0/24", "10.0.152.0/24"]

  # NAT Gateways - Outbound Communication
  enable_nat_gateway = false
  single_nat_gateway = true

  # VPC DNS Parameters
  enable_dns_hostnames = true
  enable_dns_support   = true

  public_subnet_tags = {
    Name = "beta-development-vpc-public-subnet"
  }

  private_subnet_tags = {
    Name = "beta-development-vpc-private-subnet"
  }

  database_subnet_tags = {
    Name = "beta-development-vpc-database-private-subnet"
  }

  tags = {
    Owner       = "PECS"
    Project     = "alpha"
    Environment = "development"
    Create_By   = "Terraform"
  }

  vpc_tags = {
    Name        = "beta-development-vpc"
    Owner       = "PECS"
    Project     = "alpha"
    Environment = "development"
    Create_By   = "Terraform"
  }
}

terraform {
  backend "s3" {
    bucket         = "ektec-development-terraform-state"
    key            = "terraform-backend-vpc-state/vpc2"
    region         = "us-east-1"
    dynamodb_table = "ektec-development-terraform-state-lock"
  }
}
