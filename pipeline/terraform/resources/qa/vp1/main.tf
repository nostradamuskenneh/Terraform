# Provider Block
provider "aws" {
  region = var.region
}

module "vpc" {
  source             = "../../../modules/vpc1"
  region             = "us-east-1"
  availability_zones = ["us-east-1a", "us-east-1b", "us-east-1c"]
  cidr_block         = "10.0.0.0/16"
  vpc_name           = "alpha"

  tags = {
    Owner       = "PECS"
    Project     = "alpha"
    Environment = "qa"
    Create_By   = "Terraform"
  }
}

terraform {
  backend "s3" {
    bucket         = "ektec-qa-terraform-state"
    key            = "terraform-backend-vpc-state/vpc1"
    region         = "us-east-1"
    dynamodb_table = "ektec-qa-terraform-state-lock"
  }
}
