module "vpc" {
  source = "../../../modules/vpc2"

  name = "beta-development-vpc"

  cidr = "10.0.0.0/16"

  azs             = ["us-east-1a", "us-east-1b", "us-east-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  assign_generated_ipv6_cidr_block = true

  enable_nat_gateway = true
  single_nat_gateway = true
  #one_nat_gateway_per_az = true

  public_subnet_tags = {
    Name = "beta-development-vpc-public-subnet"
  }

  private_subnet_tags = {
    Name = "beta-development-vpc-private-subnet"
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
