# Provider Block
provider "aws" {
  region = var.region
}

module "ec2" {
  source = "../../module/ec2"

  instance_name = "dev-instance"
  instance_type = "t2.micro"
  instance_key  = "s2-key"
  env           = "Development"
}

terraform {
  backend "s3" {
    bucket         = "ektec-terraform-student-state"
    key            = "dev/dev-ec2/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "ektec-terraform-student-state-lock"
  }
}

